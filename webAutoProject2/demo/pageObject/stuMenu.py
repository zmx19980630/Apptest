#coding="utf-8"
#操作学员管理页
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObject.loginPage import LoginPage


class StuMenu(LoginPage):
    ex=DoExcel("testData.xlsx","studentfile")
    # 学员档案
    mv = (By.XPATH, ex.readExcel(1,4))
    #全部学员
    qbxy=(By.XPATH,ex.readExcel(2,4))
    #待跟进学员
    gnxy=(By.XPATH,ex.readExcel(3,4))
    #在读学员
    zdxy=(By.XPATH,ex.readExcel(4,4))
    #流失学员
    lsxy= (By.XPATH, ex.readExcel(5,4))
    #输入框
    inp=(By.CSS_SELECTOR,ex.readExcel(6,4))
    #搜索按钮
    sbut=(By.CSS_SELECTOR,ex.readExcel(7,4))

    def tabFun(self):
        self.LoginFun()
        self.doClick(self.smvalue)
        self.doClick(self.mv)
        #全部学员
        self.doClick(self.qbxy)
        sleep(1)
        self.inputValue(self.inp,"1024")
        self.doClick(self.sbut)
        sleep(5)
        # 待跟进学员
        self.doClick(self.gnxy)
        sleep(1)
        self.inputValue(self.inp, "13411112222")
        self.doClick(self.sbut)
        sleep(5)
        # 在读学员
        self.doClick(self.zdxy)
        sleep(1)
        self.inputValue(self.inp,"图图老师")
        self.doClick(self.sbut)
        sleep(5)
        # 搜索按钮
        self.doClick(self.lsxy)
        sleep(1)
        self.inputValue(self.inp, "校长昵称")
        self.doClick(self.sbut)
        sleep(5)


if __name__ == '__main__':
    driver=webdriver.Chrome()
    stM=StuMenu(driver)
    stM.open()
    stM.driver.maximize_window()
    # stM.driver.implicitly_wait(10)
    stM.tabFun()
    stM.driver.quit()

