from time import sleep

import pytest, scripts as s
from api.entranceApi import EntranceApi
from base.base_pymysql import BasePymysql
from base.base_yaml import GetYaml
from base.base_log import GetLogging

log = GetLogging.get_log()


class TestFileTask:
    @classmethod
    def setup_class(cls):
        cls.ent = EntranceApi()
        cls.token = cls.ent.ent_token().getToken()
        cls.conn = BasePymysql.py_conn()
        cls.cursor = BasePymysql.py_cursor(cls.conn)
        cls.terminal = []

    @classmethod
    def teardown_class(cls):
        BasePymysql.py_close(cls.cursor, cls.conn)

    @pytest.mark.parametrize("value", GetYaml.loads("fileData", "test_file_add"))
    def test_file_add(self, value):
        log.success("获取参数：{},{},{},{}", value["taskPriority"], value["playMode"], value["volume"], value["taskName"])
        sleep(2)
        try:

            sql = s.sql_hardware
            hardwareIds = BasePymysql.py_execut_fetchall(self.cursor, sql)
            log.success("查询终端ID:{}".format(hardwareIds))

            sql = s.sql_media
            mediaFileIds = BasePymysql.py_execut_fetchall(self.cursor, sql)
            log.success("查询音频文件ID:{}".format(mediaFileIds))

            response = self.ent.ent_file_task().file_add(self.token, hardwareIds, mediaFileIds, value["taskPriority"],
                                                         value["playMode"], value["volume"], value["taskName"])

            log.success("响应内容:{}".format(response.text))
            log.success("响应状态码:{}".format(response.status_code))
            self.conn.commit()

            sql = s.sql_taskId.format(value["taskName"])
            taskId = BasePymysql.py_execut_fetchall(self.cursor, sql)
            self.terminal.append(taskId)
            log.success("通过任务名称查询ID:{}".format(self.terminal))


        except Exception as e:
            self.conn.rollback()
            print("ERRER:{}".format(e))

    def test_file_del(self):

        list = ""
        for i in self.terminal:
            list = list +","+ i
        response = self.ent.ent_file_task().file_del(token=self.token, taskIds=list[1:], taskType=160)
        log.success("删除任务ID:{}".format(list[1:]))
        log.success("响应内容:{}".format(response.text))
        log.success("响应状态码:{}".format(response.status_code))