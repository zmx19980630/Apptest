# 3.新建测试用例py文件，完成学员管理的测试用例
#   #测试用例1，学员管理页面某个的断言
#   #测试用例2，学员管理有三个下拉菜单
import logging
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from common.doLog import Logger
from demo.testCase.baseUnittest import BaseUnitTest

#定义log对象
log=Logger(__name__,logging.ERROR)
class TestStuManage(BaseUnitTest):
    #登录雷小锋-跳转学员管理
    # 工作台-学员管理
    def test_stumenu_info_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.doClick(self.loginPage.smvalue)
        sleep(3)
        #断言-招生跟进待预约
        self.loginPage.doClick(self.loginPage.dypeople)
        # 当前路径
        url = self.driver.current_url
        try:
            self.assertIn("stuFollow", url)
        except Exception as e:
            log.logger.exception("招生跟进待预约页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("招生跟进待预约页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-学员管理-学员档案
    def test_stumenu_ass_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.doClick(self.loginPage.smvalue)
        #点击学员档案
        self.loginPage.doClick(self.loginPage.mv)
        # 当前路径
        url = self.driver.current_url
        #学生档案页面
        try:
         self.assertIn("stuFile", url)
        except Exception as e:
            log.logger.exception("学生档案页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("学生档案页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-学员管理-招生跟进
    def test_stumenu_findstu_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.doClick(self.loginPage.smvalue)
        # 点击招生跟进
        self.loginPage.doClick(self.loginPage.fv)
        # 当前路径
        url = self.driver.current_url
        # 招生跟进页面
        try:
            self.assertIn("stuFollow", url)
        except Exception as e:
            log.logger.exception("招生跟进页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("招生跟进页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-学员管理-学员费用
    def test_stumenu_stumoney_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.doClick(self.loginPage.smvalue)
        # 点击学院费用
        self.loginPage.doClick(self.loginPage.smv)
        # 当前路径
        url = self.driver.current_url
        # 学院费用页面
        try:
            self.assertIn("stuFee", url)
        except Exception as e:
            log.logger.exception("学院费用页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("学院费用页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-学员管理-导入导出
    def test_stumenu_inpprint_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.doClick(self.loginPage.smvalue)
        # 点击导入导出
        self.loginPage.doClick(self.loginPage.ipv)
        # 当前路径
        url = self.driver.current_url
        # 导入导出页面
        try:
            self.assertIn("importStuMenu", url)
        except Exception as e:
            log.logger.exception("导入导出页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("导入导出页面断言成功！")
            self.loginPage.doPhotos("_pass")

if __name__ == '__main__':
    unittest.main()
