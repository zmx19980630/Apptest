#coding="utf-8"
#操作学员管理页
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObject.loginPage import LoginPage


class StuManage(LoginPage):
    ex = DoExcel("testData.xlsx","studentmanage")
    #学员档案
    mv=(By.XPATH,ex.readExcel(1,4))
    #招生跟进
    fv=(By.XPATH,ex.readExcel(2,4))
    #学员费用
    smv=(By.XPATH,ex.readExcel(3,4))
    #导入、导出
    ipv= (By.XPATH, ex.readExcel(4,4))


    def menuFun(self):
        self.LoginFun(self.loginDatalist[0][0],self.loginDatalist[0][1])
        self.doClick(self.smvalue)
        self.doClick(self.mv)
        self.doClick(self.fv)
        self.doClick(self.smv)
        self.doClick(self.ipv)


if __name__ == '__main__':
    driver=webdriver.Chrome()
    stM=StuManage(driver)
    stM.open()
    stM.driver.maximize_window()
    stM.driver.implicitly_wait(10)
    stM.menuFun()
    stM.driver.quit()

