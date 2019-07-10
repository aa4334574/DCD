import pymysql.cursors
import time
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
    # def time_change(self,start_time,end_time):
    #     start_time1 = time.strptime(start_time,"%Y-%m-%d %H:%M:%S")
    #     end_time1 = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    #     print(start_time1-end_time1)


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
            start_time = time.time()
            print('开始时间%s'%start_time)
            execute_mum = self.cursor.execute(sql)
            end_time = time.time()
            print('结束时间%s'%end_time)
            print(execute_mum,time.localtime(end_time-start_time))
        except Exception as e:
            log().logger.exception('e')
        return self.cursor.fetchall()


    def close(self):
        self.connect.close()


sql = 'select * from datafile limit 1000'
message = mysql().select(sql)
for i in message:
    print(i[3])
# for i in message:
#     tem = 0
#     for j in i:
#         tem += 1
#         if tem == 3:
#             print(j)
#


# #

# cursor.execute(sql)
# print((cursor.fetchall(),cursor.rowcount))
# for i in cursor.fetchall():
#     print (i)
# print(cursor.fetchall())
