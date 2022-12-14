#coding="utf-8"
#基础页面类：存放所有页面可能用到的公共方法及属性
#所有page类均继承该基础类
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common import config
from common.doExcel import DoExcel
from common.doLog import Logger



#定义log对象
log=Logger(__name__,logging.DEBUG)
#定义数据驱动
ex1=DoExcel("testData.xlsx","elements")
ex2=DoExcel('testData.xlsx',"loginData")
ex3= DoExcel("testData.xlsx", "studentmanage")
class BasePage(object):

    #定位登录成功后右上角退出登录
    #右上角的个人头像
    img=(By.CSS_SELECTOR,ex1.readExcel(8,4))
    #退出账号
    logout=(By.XPATH,ex1.readExcel(9,4))
    #退出账号的弹窗确定按钮
    logoutOk=(By.CSS_SELECTOR,ex1.readExcel(10,4))
    # 个人信息
    personinfo = (By.XPATH, ex1.readExcel(18, 4))
    #个人信息-name
    pername=(By.XPATH,ex1.readExcel(19,4))
    #个人信息-手机号
    pernumber=(By.XPATH,ex1.readExcel(20,4))
    #工作台
    clvalue=(By.XPATH,ex1.readExcel(11,4))
    #学员管理
    smvalue=(By.XPATH,ex1.readExcel(12,4))
    #教务管理
    thvalue=(By.XPATH,ex1.readExcel(13,4))
    #机构管理
    ogvalue=(By.XPATH,ex1.readExcel(14,4))
    #数据分析
    datavalue=(By.XPATH,ex1.readExcel(15,4))
    #招生吧
    fdvalue=(By.XPATH,ex1.readExcel(16,4))
    #考级管理
    examvalue=(By.XPATH,ex1.readExcel(17,4))

    # 学员档案
    mv = (By.XPATH, ex3.readExcel(1, 4))
    # 招生跟进
    fv = (By.XPATH, ex3.readExcel(2, 4))
    # 学员费用
    smv = (By.XPATH, ex3.readExcel(3, 4))
    # 导入、导出
    ipv = (By.XPATH, ex3.readExcel(4, 4))
    #待预约
    dypeople = (By.CSS_SELECTOR, ex3.readExcel(5,4))
    #重构初始方法
    def __init__(self,driver,url=config.base_url):
        self.driver=driver
        self.url=url


    #打开页面
    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            # print("出现异常，页面打开失败，失败内容是：%s\n失败的页面是：%s"%(e,self.url))
            log.logger.critical("出现异常，页面打开失败，失败内容是：%s\n失败的页面是：%s"%(e,self.url),exc_info=True)
        else:
            # print("页面打开成功，未发生异常：%s"%self.url)
            log.logger.info("页面打开成功，未发生异常：%s"%self.url)
    #定位元素
    def findElement(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).\
                until(EC.visibility_of_element_located(locater))
        except Exception as e:
            print("出现异常，定位失败\n错误信息是：%s,该元素是：%s"%(e,str(locater)))
            log.logger.error("出现异常，定位失败\n错误信息是：%s,该元素是：%s"%(e,str(locater)),exc_info=True)
        else:
            print("元素定位成功,该元素是：%s"%str(locater))
            log.logger.info("元素定位成功,该元素是：%s"%str(locater))
            return ele
    #文本框输入
    def inputValue(self,inputBox,value):
        ele=self.findElement(*inputBox)
        try:
            ele.send_keys(value)
        except Exception as e:
            print("出现异常，输入%s失败\n原因是：%s"%(value,e))
            log.logger.error("出现异常，输入%s失败\n原因是：%s"%(value,e),exc_info=True)
        else:
            print("输入内容%s成功！！！"%value)
            log.logger.info("输入内容%s成功！！！"%value)
    #获取标签值
    def getElementValue(self,element):
        #定位元素
        ele=self.findElement(*element)
        #获取元素文本
        try:
           eleText=ele.text
        except Exception as e:
            print("出现异常，获取文本%s失败,\n错误信息是：%s"%(str(element),e))
            log.logger.error("出现异常，获取文本%s失败,\n错误信息是：%s"%(str(element),e),exc_info=True)
        else:
            print("文本获取成功：%s"%eleText)
            log.logger.info("文本获取成功：%s"%eleText)
            return eleText


    #截图
    def doPhotos(self,name):
        filename=config.photo_path+config.cur_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            print("出现异常，截图失败，失败信息是：%s"%e)
            log.logger.error("出现异常，截图失败，失败信息是：%s"%e,exc_info=True)
        else:
            print("截图成功！！！")
            log.logger.info("截图成功！！！")

    #元素点击
    def doClick(self,element):
        ele=self.findElement(*element)
        try:
            # ele.click()
            self.driver.execute_script("arguments[0].click();", ele)#jquery脚本级别的语言进行点击，获取第0个元素。源码级别的代码
        except Exception as e:
            print("出现异常，点击该元素%s失败\n错误信息是：%s"%(str(element),e))
            log.logger.error("出现异常，点击该元素%s失败\n错误信息是：%s"%(str(element),e),exc_info=True)
        else:
            print("点击成功！！！")
            log.logger.info("点击成功！！！")

     #退出登录
    def logOutFun(self,driver):
        action=ActionChains(driver)
        action.move_to_element(self.findElement(*self.img))
        action.perform()
        #点击退出登录按钮
        self.doClick(self.logout)
        #点击弹窗中确定按钮
        self.doClick(self.logoutOk)
        sleep(3)
    #点击个人信息
    def personFun(self):
        #鼠标悬浮
        self.mouseFun(self.driver)
        #点击个人信息
        self.doClick(self.personinfo)
    #鼠标悬浮
    def mouseFun(self,driver):
        action = ActionChains(driver)
        action.move_to_element(self.findElement(*self.img))
        action.perform()

if __name__ == '__main__':
    driver=webdriver.Chrome()
    # url="http://www.baidu.com"
    basepg=BasePage(driver)
    # #调用open方法
    basepg.open()
    basepg.driver.maximize_window()
    basepg.driver.implicitly_wait(10)
    #
    # #定位输入框
    locater=(By.ID,"kw")
    basepg.inputValue(locater,"python")

    #输出文本标签值
    locater=(By.LINK_TEXT,"设置")
    basepg.getElementValue(locater)
    #点击设置按钮
    basepg.doClick(locater)

    #截图
    basepg.doPhotos("2")



























