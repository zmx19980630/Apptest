#coding="utf-8"
#处理不同的测试报告
import logging
from unittest import TextTestRunner

from HTMLTestRunner import HTMLTestRunner
from htmltestreport import HTMLTestReport

from common import config
from common.doLog import Logger

#生成text格式的测试报告
log=Logger(__name__,logging.ERROR)
def doTextReport(suite):
    filename=config.report_path+config.cur_time+"_report.txt"
    #通过with打开，不用时自动关闭-----防止打开文件（它是以文件流的形式）忘记关闭
    #open()以写的形式存入filename中
    try:
        with open(filename,"w",encoding="utf-8") as f:
            runner=TextTestRunner(stream=f,verbosity=2)
            runner.run(suite)
    except Exception as e:
        log.logger.exception("报告生成失败，原因是：%s"%e,exc_info=True)#显示完整的异常信息
    else:
        log.logger.info("报告生成成功！")

#生成HTML格式的测试报告
def doHTMLReport(suite):
    filename=config.report_path+config.cur_time+"_report.html"
    # 通过with打开，不用时自动关闭-----防止打开文件（它是以文件流的形式）忘记关闭
    # open()以二进制流wb(可以加载图片)的打开，重新写入filename
    try:
        with open(filename,"w",encoding="utf-8") as f:
            runner=HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,
                                                 title="雷小锋项目测试报告",description="html格式的测试报告,v1.0版本")
            runner.run(suite)
    except Exception as e:
        log.logger.exception("html格式的测试报告生成失败，原因是：%s"%e,exc_info=True)
    else:
        log.logger.info("html格式的测试报告生成成功！")

#生成更美观格式的测试报告---HTMLTestReport
def doHTMLReport_more(suite):
    filename=config.report_path+config.cur_time+"_morereport.html"
    runner=HTMLTestReport(filename,title="雷小锋项目测试报告",description="更全html格式的测试报告,v1.0版本")
    runner.run(suite)

























































































































