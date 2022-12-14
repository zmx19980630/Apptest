#coding="utf-8"
#处理excel文件
import logging

import xlrd

from common import config
from common.doLog import Logger

log=Logger(__name__,logging.DEBUG)
class DoExcel(object):
    #重构初始化方法
    def __init__(self,wk,st):
        #定义文件名
        filename=config.data_path+wk
        #打开工作簿
        try:
            self.workbook=xlrd.open_workbook(filename)
        except Exception as e:
            log.logger.error("文件打开异常！！，错误信息是：%s"%e)
        else:
            log.logger.info("文件打开成功！！")
        # #获取sheet页,三种方式获取sheet页
        # stnames = self.workbook.sheet_names()
        # print(stnames)
        # #第一种方式，列表的下标
        # self.sheet = stnames[0]
        # #第二种方式，索引 index
        # self.sheet=self.workbook.sheet_by_index(0)
        # self.stnames = self.workbook.sheet_names()[0]
        #第三种方式，sheet名称

        try:
            self.sheet=self.workbook.sheet_by_name(st)
        except Exception as e:
            log.logger.error("sheet表获取异常，错误信息是：%s"%e,exc_info=True)
        else:
            log.logger.info("sheet表获取成功！！")
    def readExcel(self,rownum,colnum):
        try:
            value=self.sheet.cell_value(rownum,colnum)
        except Exception as e:
            print("读取文件异常:%s"%e)
            log.logger.error("文件读取异常:%s，请重新再试！"%e,exc_info=True)
        else:
            log.logger.info("读取文件成功，值是：%s"%value)
            return value

    #读取单元格的值




if __name__ == '__main__':
    ex=DoExcel('testData.xlsx',"elements")
    value=ex.readExcel(1, 4)
    print(value)
    print(ex.readExcel(1, 3))





















