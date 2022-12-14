#coding="utf-8"
#百度登录页面
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObject.basePage import BasePage


class BaiduLogin(BasePage):
     ex=DoExcel()
     #定位登录按钮
     but=(By.ID,ex.readExcel(1,4))
     #登录输入框
     username=(By.ID,ex.readExcel(2,4))
     #登录密码
     password=(By.ID,ex.readExcel(3,4))
     #登录按钮
     loginbut=(By.ID,ex.readExcel(4,4))
     #错误信息
     errortext=(By.CSS_SELECTOR,ex.readExcel(5,4))
     def login(self,us,pw):
          #点击登录按钮
          self.doClick(self.but)
          #用户输入框
          self.inputValue(self.username,us)
          #密码输入框
          self.inputValue(self.password,pw)
          #点击立即登录按钮
          self.doClick(self.loginbut)


if __name__ == '__main__':
    driver=webdriver.Chrome()
    url="https://www.baidu.com/"
    bdlogin=BaiduLogin(driver,url)
    #打开百度页面
    bdlogin.open()
    bdlogin.driver.maximize_window()
    bdlogin.driver.implicitly_wait(10)
    #登录页面
    bdlogin.login("","")
    sleep(3)
    #登录失败---错误信息
    erT=bdlogin.getElementValue(bdlogin.errortext)
    print(erT)
    bdlogin.driver.quit()
