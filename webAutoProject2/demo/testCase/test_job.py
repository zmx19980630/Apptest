# 2.新建测试用例py文件，完成工作台的测试用例
#   #用例1：工作台页面个人信息元素的断言
#   #用例2：左侧菜单列表的断言
import logging
import unittest
from time import sleep

from common.doLog import Logger
from demo.testCase.baseUnittest import BaseUnitTest

#定义log对象
log=Logger(__name__,logging.ERROR)
class TestJob(BaseUnitTest):
    #工作台页面鼠标悬浮个人信息按钮的断言
    def test_psinfo_url_ok(self):
        #登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        #点击工作台-个人信息
        self.loginPage.personFun()
        sleep(1)
        #登录后的url
        url=self.driver.current_url
        #判断页面跳转
        try:
            self.assertIn("self",url)
        except Exception as e:
            log.logger.exception("个人信息页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("个人信息按钮断言成功！")
            self.loginPage.doPhotos("_pass")


    # 工作台页面个人信息元素姓名的断言
    def test_psinfo_name_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 查看姓名断言
        nametext=self.loginPage.getElementValue(self.loginPage.pername)
        try:
            self.assertEqual("龚老师1",nametext)
        except Exception as e:
            log.logger.exception("个人信息页面姓名断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("个人信息姓名断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台页面个人信息元素手机号的断言
    def test_psinfo_number_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 查看手机号断言
        numbertext = self.loginPage.getElementValue(self.loginPage.pernumber)
        try:
            self.assertEqual("13986128128", numbertext)
        except Exception as e:
            log.logger.exception("个人信息页面手机号断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("个人信息手机号断言成功！")
            self.loginPage.doPhotos("_pass")



    #菜单断言
    #工作台-学员管理
    def test_stumenu_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        #点击学员管理
        self.loginPage.doClick(self.loginPage.smvalue)
        sleep(3)
        #当前路径
        url=self.driver.current_url
        #学员管理页面
        try:
            self.assertIn("stuAdmin", url)
        except Exception as e:
            log.logger.exception("学员管理断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("学员管理断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-教务管理
    def test_techmenu_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击教务管理
        self.loginPage.doClick(self.loginPage.thvalue)
        sleep(1)
        # 当前路径
        url = self.driver.current_url
        # 教务管理页面
        try:
         self.assertIn("jiaowuAdmin", url)
        except Exception as e:
            log.logger.exception("教务管理断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("教务管理页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-机构管理
    def test_organmenu_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击机构管理
        self.loginPage.doClick(self.loginPage.ogvalue)
        sleep(1)
        # 当前路径
        url = self.driver.current_url
        # 机构管理页面
        try:
            self.assertIn("orgAdmin", url)
        except Exception as e:
            log.logger.exception("机构管理断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("机构管理页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-数据分析
    def test_dataanaly_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击数据分析
        self.loginPage.doClick(self.loginPage.datavalue)
        sleep(1)
        # 当前路径
        url = self.driver.current_url
        # 数据分析页面
        try:
         self.assertIn("analysisMain", url)
        except Exception as e:
            log.logger.exception("数据分析页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("数据分析页面断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-招生吧
    def test_findstu_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击招生吧
        self.loginPage.doClick(self.loginPage.fdvalue)
        sleep(1)
        # 当前路径
        url = self.driver.current_url
        # 招生吧页面
        try:
         self.assertIn("admissionsMain", url)
        except Exception as e:
            log.logger.exception("招生吧页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("招生吧断言成功！")
            self.loginPage.doPhotos("_pass")

    # 工作台-考级管理
    def test_kjmanage_ok(self):
        # 登录雷小锋
        self.loginPage.LoginFun()
        sleep(1)
        # 点击考级管理
        self.loginPage.doClick(self.loginPage.examvalue)
        sleep(1)
        # 当前路径
        url = self.driver.current_url
        # 考级管理页面
        try:
            self.assertIn("kaoJiAdmin", url)
        except Exception as e:
            log.logger.exception("考级管理页面断言出现异常，异常是：%s"%e,exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("考级管理页面断言成功！")
            self.loginPage.doPhotos("_pass")

if __name__ == '__main__':
    unittest.main()
