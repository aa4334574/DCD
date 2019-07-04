import pymysql.cursors
from DCD_test.common.deal_file import log
#连接数据库
# connect = pymysql.connect(
#         host = '124.193.177.45',
#         port = 50681,
#         user = 'root',
#         password = 'db(*)2016',
#         db = 'aqr_develop_v3',
# )
# cursor = connect.cursor()

class mysql():
    def __init__(self):
        self.connect = pymysql.connect(
        host = '124.193.177.45',
        port = 50681,
        user = 'root',
        password = 'db(*)2016',
        db = 'aqr_develop_v3')
        self.cursor = self.connect.cursor()

    def update(self,sql):
        success = True
        try:
            execute_mum = self.cursor.execute(sql)
            self.connect.commit()
            print(execute_mum)
        except Exception as e:
            log().logger.exception('e')
            success = False
        return (success)

    def select(self,sql):
        try:
            execute_mum = self.cursor.execute(sql)
            print(execute_mum)

        except Exception as e:
            log().logger.exception('e')
        return self.cursor.fetchall()


    def close(self):
        self.connect.close()
sql = 'select * from datafile limit 1000'
# print(mysql().select(sql))
message = mysql().select(sql)

for i in message:
    print (i)


# #

# cursor.execute(sql)
# print((cursor.fetchall(),cursor.rowcount))
# for i in cursor.fetchall():
#     print (i)
# print(cursor.fetchall())
