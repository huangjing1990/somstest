import pymysql
from Common.log_Common import *
from Conf.Config import *


class MyDB:

    def __init__(self):

        self.config = Config()
        self.db = None
        self.cursor = None
        self.host = self.config.dbhost_debug
        self.username = self.config.dbuser_debug
        self.password = self.config.dbpassword_debug
        self.port = self.config.dbport_debug
        self.database = self.config.dbdatabase_debug
        self.config = {
            'host': str(self.host),
            'user': self.username,
            'passwd': self.password,
            'port': int(self.port),
            'db': self.database
        }

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**self.config)
            # create cursor
            self.cursor = self.db.cursor()
            LOG.info("Connect DB successfully!")
        except ConnectionError as ex:
            LOG.error(str(ex))

    def executeSQL(self, sql, params):
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

        # 获取当前查询SQL返回值

    def query(self, sql):
        conn = pymysql.connect(**self.config)
        cur = conn.cursor()
        cur.execute(sql)
        index = cur.description
        result_data = []
        for res in cur.fetchall():
            row = {}
            for i in range(len(index)):
                row[index[i][0]] = res[i]
                result_data.append(row)
        return result_data

    def closeDB(self):
        self.db.close()
        LOG.info("Database closed!")


if __name__ == '__main__':
    print(MyDB().query("SELECT user_name,user_password from dbshop_user limit 1"))
