import pytest, scripts as s

from api.entranceApi import EntranceApi
from base.base_pymysql import BasePymysql
from base.base_yaml import GetYaml
from base.base_log import GetLogging

log = GetLogging.get_log()


class TestTiming:
    @classmethod
    def setup_class(cls):
        log.success("——————————> 初始化【定时方案】接口资源")
        cls.ent = EntranceApi()
        cls.projeck = cls.ent.ent_project_task()
        cls.timingTask = cls.ent.ent_timing_task()
        cls.token = cls.ent.ent_token().getToken()
        cls.conn = BasePymysql.py_conn()
        cls.cursor = BasePymysql.py_cursor(cls.conn)
        cls.terminal = []


    @classmethod
    def teardown_class(cls):
        BasePymysql.py_close(cls.cursor, cls.conn)


    @pytest.mark.run(oder=10)
    @pytest.mark.parametrize("value", GetYaml.loads("timingData", "test_timing_add"))
    def test_projeck_add(self, value):
        # 添加定时方案
        self.projeck.timing_project_add(self.token, value["planName"], value["beginDate"], value["endDate"])
        sql = s.sql_timing_projeckID.format(value["planName"])

        global projeckID
        projeckID = BasePymysql.py_execut_fetchall(self.cursor, sql=sql)

        self.terminal.append(projeckID)
        log.success("获取定时方案ID：{}".format(self.terminal))


    @pytest.mark.run(oder=20)
    @pytest.mark.parametrize("value", GetYaml.loads("timingData", "test_timing_task_add"))
    def test_timing_task_add(self, value):
        taskHardwareId = s.sql_hardware
        # 添加定时任务
        self.timingTask.timing_t_task_add(self.token, planId=projeckID, taskHardwareId=taskHardwareId,
                                          taskName=value["taskName"],
                                          timedExecuteType=value["timedExecuteType"],
                                          weeks=value["weeks"], executeTime=value["executeTime"],
                                          continueTime=value["continueTime"], taskPriority=value["taskPriority"],
                                          taskMediaFileId=value["taskMediaFileId"],
                                          playMode=value["playMode"], taskVolume=value["taskVolume"],
                                          taskType=value["taskType"], speechData=value["speechData"],
                                          captureType=value["captureType"])


    @pytest.mark.run(oder=30)
    def test_del(self):
        list = ""
        for i in self.terminal:
            list = list + "," + i

        response = self.projeck.timing_project_del(self.token, list[1:])
        log.success("删除定时方案ID:{}".format(list[1:]))
        log.success("响应内容:{}".format(response.text))
        log.success("响应状态码:{}".format(response.status_code))
