import pymysql.cursors

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

    def select(self,sql):
        try:
            a=self.cursor.execute(sql1)
        except Exception as e:
            print(e)
        return (self.cursor.fetchall(),a.rowcount)


sql = r'select  * from content   order by  id desc  limit 10'
mysql.select(sql)

# #

# cursor.execute(sql)
# print((cursor.fetchall(),cursor.rowcount))
# for i in cursor.fetchall():
#     print (i)
# print(cursor.fetchall())
