#coding="utf-8"
#基础的unittest,前置后置方法

import unittest

from selenium import webdriver

from demo.pageObject.loginPage import LoginPage
from demo.pageObject.stuManage import StuManage


class BaseUnitTest(unittest.TestCase):
    #类方法的前置,cls表示类自身，表示一个实例
    @classmethod   #代表类级别的方法
    def setUpClass(cls) -> None:
        #实例化浏览器
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()


    #类方法的后置
    @classmethod
    def tearDownClass(cls) -> None:
        #退出浏览器
        cls.driver.quit()


    #方法级别的前置
    def setUp(self) -> None:
        #实例化登录页面--------每个py页都需要传入driver，所以传入driver
        self.loginPage=LoginPage(self.driver)
        #打开页面
        self.loginPage.open()
        #实例化菜单
        self.stumenu=StuManage(LoginPage)
        


    #方法级别的后置
    def tearDown(self) -> None:
        #刷新页面
        self.driver.refresh()



































