# confing="utf-8"
# 定义登录函数
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common import config

from demo.pageObject.basePage import BasePage, ex1,ex2


class LoginPage(BasePage):

    # 用户名
    unnameLocater = (By.CSS_SELECTOR,ex1.readExcel(1,4))
    # 密码
    upwdLocater = (By.CSS_SELECTOR, ex1.readExcel(2,4))
    # 登录按钮
    butLocater = (By.CSS_SELECTOR, ex1.readExcel(3,4))

    # 错误信息-登录失败的信息提示-小窗

    erroruname = (By.XPATH, ex1.readExcel(4,4))
    errorpwd = (By.XPATH, ex1.readExcel(5, 4))


    errortext=(By.CSS_SELECTOR, ex1.readExcel(6,4))
    #小窗的确定按钮

    acceptBut=(By.CSS_SELECTOR, ex1.readExcel(7,4))

    #登录数据
    loginDatalist=[[ex2.readExcel(1, 3), ex2.readExcel(1, 4)],#正确的用户名，密码
                   [ex2.readExcel(2, 3), ex2.readExcel(2, 4)],#用户名空，密码空
                   [ex2.readExcel(3, 3), ex2.readExcel(3, 4)],#用户名空，密码非空
                   [ex2.readExcel(4, 3), ex2.readExcel(4, 4)],#用户名非空，密码空
                   [ex2.readExcel(5, 3), ex2.readExcel(5, 4)],#用户名错误，密码正确
                   [ex2.readExcel(6, 3), ex2.readExcel(6, 4)],#用户名正确，密码错误
                   [ex2.readExcel(7, 3), ex2.readExcel(7, 4)],#用户名错误，密码错误
                   [ex2.readExcel(8, 3), ex2.readExcel(8, 4)],#用户名长度不够，密码正确
                   [ex2.readExcel(9, 3), ex2.readExcel(9, 4)],#用户名长度超出12位，密码正确
                   [ex2.readExcel(10, 3), ex2.readExcel(10, 4)],#用户名长度正确，密码不够
                   [ex2.readExcel(11, 3), ex2.readExcel(11, 4)],#用户名长度正确，密码超出20位
                   [ex2.readExcel(12, 3), ex2.readExcel(12, 4)],#用户名长度超过12位，密码超出21位
                   [ex2.readExcel(13, 3), ex2.readExcel(13, 4)]#用户名长度不够，密码长度不够
                   ]

    # 登录方法
    def LoginFun(self, vname=loginDatalist[0][0],
                       vpwd=loginDatalist[0][1]):
        # 输入用户名
        self.inputValue(self.unnameLocater, vname)
        # 输入密码
        self.inputValue(self.upwdLocater, vpwd)
        # 点击登录按钮
        self.doClick(self.butLocater)
        sleep(5)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # url = config.base_url
    login = LoginPage(driver)
    login.open()
    login.driver.maximize_window()
    login.driver.implicitly_wait(10)
    # login.LoginFun()
    # login.logOutFun(driver)
    # #登录成功
    login.LoginFun()
    # #账号登录失败
    # #获取错误信息的值，并打印
    # # errorname=log.getElementValue(log.erroruname)
    # # print(errorname)
    # # errorpwd=log.getElementValue(log.errorpwd)
    # # print(errorpwd)
    # errText=login.getElementValue(login.errortext)
    # print(errText)
    # login.doClick(login.acceptBut)
    login.logOutFun(driver)
    login.driver.quit()
    # print(login.loginDatalist)




























