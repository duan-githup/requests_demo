import pymysql

class BasePymysql:

    @classmethod
    def py_conn(self,user="root",password="123456",host="192.168.3.244",database="sit_cloudbc"):
        # 获取连接
        # 自动提交事务autocommit = True
        return pymysql.Connect(user=user,password=password,
                               host=host,database=database,port=3306,charset="utf8")

    @classmethod
    def py_cursor(self,conn):
        # 获取游标
        return conn.cursor()

    @classmethod
    def py_execut_fetchall(self,cursor,sql):
        """获取值的列表"""
        cursor.execute(sql)
        value = ""
        for i in cursor.fetchall():
            value = value + "," + str(i[0])
        return value[1:]

    @classmethod
    def py_execut_fetchone(self, cursor, sql):
        """获取单个值"""
        cursor.execute(sql)
        value = cursor.fetchone()
        return value[0]

    @classmethod
    def py_close(self,cursor,conn):
        # 释放资源
        cursor.close()
        conn.close()


if __name__ == '__main__':
    sql = 'select role_id from t_role;'
    p = BasePymysql()
    conn = p.py_conn()
    cursor = p.py_cursor(conn)
    data = p.py_execut_fetchall(cursor,sql)
    print(data)
    p.py_close(cursor,conn)
