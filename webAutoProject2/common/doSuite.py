#coding="utf-8"
#testsuite的添加方式
import unittest

from common import config
from demo.testCase.test_login import TestLogin


#通过测试类及测试方法添加用例
def addTestByMethon(suite):
    #添加测试用例到suite
    suite.addTest(TestLogin("test_user_pwd_ok"))
    suite.addTest(TestLogin("test_user_no_pwd_none"))
    print(suite)
    return suite

def addTestByClass(suite):
    suite.addTest\
        (unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))
    return suite
#使用第三种方式获取装满用例的箱子--------会自动生成一个对象
def addTestByAuto():
    suite=unittest.TestLoader().discover(config.test_path,pattern="test*.py")
    return suite
#定义空箱子
suite1=unittest.TestSuite()
#向空箱子添加用例，通过一个个用例名添加
#箱子里添加用例后，让他的名称，重命suite2
suite2=addTestByMethon(suite1)
#打印出装好用例的箱子内容
print("我调用的是第一个方法",suite2)

#向空箱子添加用例，通过测试用例类名称的形式添加
#箱子里添加用例后，让他的名称，重命suite3
suite3=addTestByClass(suite1)
#打印出装好用例的箱子内容
print("我调用的是第二个方法",suite3)

#通过py文件自动匹配的方式，集合用例并打包成一个箱子
suite4=addTestByAuto()
print("我调用的是第三个方法",suite4)














































































































