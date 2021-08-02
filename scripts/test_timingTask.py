import pytest

from api.entranceApi import EntranceApi
from base.base_pymysql import BasePymysql


class TestTiming:
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

    @pytest.mark.parametrize()
    def test_projeck_add(self):
        projeck = self.ent.ent_project_task()
        projeck.timing_project_add()


    def test_del(self):
        print("222222")