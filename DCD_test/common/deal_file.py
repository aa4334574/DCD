import os
import requests
import xlrd
import logging
from logging import config
import time
class Deal_file:
    def __init__(self,path):
        self.path = path

    def write_excel(self):

        readbook = xlrd.open_workbook(self.path)
        sheet = readbook.sheet_by_index(0)
        nrows = sheet.nrows
        dic = {}
        for i in range(nrows):
            key = sheet.cell(i,0).value#获取第1列行第i行的表格值22222
            value = sheet.cell(i,1).value#获取第2列第i行的表格值
            dic['key'] = value
        return dic


class log():
    def __init__(self):
        # 读取日志配置文件内容
        logging.config.fileConfig('logging.conf')
        # 创建一个日志器logger
        self.logger = logging.getLogger()

# 日志输出

# try:
#     a= b
# except Exception as e:
#     log().logger.exception('e')

    # log().logger.exception(e)
# log().logger.debug('debug message')
# log().logger.info('info message')
# log().logger.warn('warn message')
# log().logger.error('error message')
# log().logger.critical('critical message')


#
# print (type(Deal_file(r'D:\可知新资源\1223\22.xlsx').write_excel()))