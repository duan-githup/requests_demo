import pytest,scripts as s

from api.entranceApi import EntranceApi
from base.base_pymysql import BasePymysql
from base.base_yaml import GetYaml
from base.base_log import GetLogging

log = GetLogging.get_log()


class TestTimingProject:
    @classmethod
    def setup_class(cls):
        log.success("——————————> 初始化【定时方案】接口资源")
        cls.ent = EntranceApi()
        cls.projeck = cls.ent.ent_project_task()
        cls.token = cls.ent.ent_token().getToken()
        cls.conn = BasePymysql.py_conn()
        cls.cursor = BasePymysql.py_cursor(cls.conn)
        cls.terminal = []

    @classmethod
    def teardown_class(cls):
        BasePymysql.py_close(cls.cursor, cls.conn)

    @pytest.mark.parametrize("value",GetYaml.loads("timingData","test_timing_add"))
    def test_projeck_add(self,value):

        self.projeck.timing_project_add(self.token,value["planName"],value["beginDate"],value["endDate"])

        sql = s.sql_timing_projeckID.format(value["planName"])
        projeckID = BasePymysql.py_execut_fetchall(self.cursor,sql=sql)
        self.terminal.append(projeckID)
        log.success("获取定时方案ID：{}".format(self.terminal))


    def test_del(self):

        list = ""
        for i in self.terminal:
            list = list + "," + i

        response = self.projeck.timing_project_del(self.token,list[1:])
        log.success("删除定时方案ID:{}".format(list[1:]))
        log.success("响应内容:{}".format(response.text))
        log.success("响应状态码:{}".format(response.status_code))