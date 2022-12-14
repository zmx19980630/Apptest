#conding="utf-8"
#登录页面测试用例类
import logging
import unittest
from time import sleep

from common.doLog import Logger
from demo.testCase.baseUnittest import BaseUnitTest

#定义log对象
log=Logger(__name__,logging.ERROR)
class TestLogin(BaseUnitTest):
    #第一步执行的代码：setUpClass()类前置
    #第二步执行的代码：setUp()     方法前置
    #第三步执行的代码是测试方法  ok
    #第四步执行测试方法的代码，直到完毕
    #第五步执行代码：tearDown() 方法后置
    #第六步找还没有执行的代码，有的话，执行方法前置setUp()
    #第七步，第六步有的话，执行测试方法中的代码，直到完毕
    #第八步，第六步有的话，执行tearDown()方法
    #第九步，找还有没有测试方法，无的话，执行的代码是：tearDownClass()类后置
    def test_user_pwd_ok(self):
        self.loginPage.LoginFun()
        self.driver.implicitly_wait(10)
        sleep(3)
        #获取登录成功后的url
        self.url=self.driver.current_url
        #判断登录
        try:
            self.assertIn("dashboard",self.url)
        except Exception as e:
            log.logger.exception("登录成功断言出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("登录成功页面断言成功！")
            self.loginPage.doPhotos("_pass")
            #退出登录
            self.loginPage.logOutFun(self.driver)

        #用户名和密码为空
    def test_user_no_pwd_none(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[1][0],
                                self.loginPage.loginDatalist[1][1])
        sleep(1)
        #判断登录失败
        # #判断手机号
        nameText=self.loginPage.getElementValue(self.loginPage.erroruname)
        try:
            self.assertEqual("请输入手机号码",nameText)
        except Exception as e:
            log.logger.exception("请输入手机号码提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("请输入手机号码文本提示成功出现！")
            self.loginPage.doPhotos("_pass")
        # #判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.errorpwd)
        try:
            self.assertEqual("请输入6-20位账户密码",pwdText)
        except Exception as e:
            log.logger.exception("请输入6-20位账户密码提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("请输入6-20位账户密码文本成功出现！")
            self.loginPage.doPhotos("_pass")

    #登录失败--用户名空，密码正确
    def test_user_none_pwd_ok(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[2][0],
                                self.loginPage.loginDatalist[2][1])
        sleep(1)
        #判断登录失败
        # #判断手机号
        nameText=self.loginPage.getElementValue(self.loginPage.erroruname)
        try:
            self.assertEqual("请输入手机号码",nameText)
        except Exception as e:
            log.logger.exception("手机号输入为空提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("手机号文本提示成功出现！")
            self.loginPage.doPhotos("_pass")

    #登录失败，用户名正确，密码空
    def test_user_ok_pwd_none(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[3][0],
                                self.loginPage.loginDatalist[3][1])
        sleep(1)
        # #判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.errorpwd)
        try:
            self.assertEqual("请输入6-20位账户密码",pwdText)
        except Exception as e:
            log.logger.exception("密码输入为空提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("密码提示文本成功出现！")
            self.loginPage.doPhotos("_pass")


    #登录失败，用户名错误，(用户名不存在)，密码正确
    def test_user_flase_pwd_true(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[4][0],
                                self.loginPage.loginDatalist[4][1])
        #判断错误
        errText = self.loginPage.getElementValue(self.loginPage.errortext)
        try:
            self.assertIn("用户名或密码错误",errText)
        except Exception as e:
            log.logger.exception("用户名或密码错误提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("用户名或密码错误文本成功出现！")
            self.loginPage.doPhotos("_pass")
            sleep(1)
            self.loginPage.doClick(self.loginPage.acceptBut)

    # 登录失败，用户名正确，密码错误
    def test_user_true_pwd_flase(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[5][0],
                                self.loginPage.loginDatalist[5][1])
        #判断错误
        errText = self.loginPage.getElementValue(self.loginPage.errortext)
        # 弹窗提醒错误的信息
        try:
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("用户名或密码错误提示文本出现异常，异常是：%s"%e, exc_info=True)
        else:
            log.logger.info("用户名或密码错误文本成功出现！")
            sleep(1)
            # 弹窗确定按钮
            self.loginPage.doClick(self.loginPage.acceptBut)

    # 登录失败，用户名错误，密码错误
    def test_user_flase_pwd_flase(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[6][0],
                                self.loginPage.loginDatalist[6][1])
        # 判断错误
        errText = self.loginPage.getElementValue(self.loginPage.errortext)
        #弹窗提醒错误的信息
        try:
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("用户名或密码错误提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("用户名或密码错误成功出现！")
            self.loginPage.doPhotos("_pass")
            sleep(1)
            #弹窗确定按钮
            self.loginPage.doClick(self.loginPage.acceptBut)

    # 登录失败，用户名长度不够，密码正确
    def test_user_short_pwd_ok(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[7][0],
                                self.loginPage.loginDatalist[7][1])
        sleep(1)
        #判断手机号
        nameText = self.loginPage.getElementValue(self.loginPage.erroruname)
        try:
            self.assertEqual("请输入手机号码", nameText)
        except Exception as e:
            log.logger.exception("请输入手机号码提示文本出现异常，异常是：%s"%e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("请输入手机号码文本成功出现！")
            self.loginPage.doPhotos("_pass")


    # 登录失败，用户名长度不够，密码正确
    def test_user_long_pwd_ok(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[8][0],
                                self.loginPage.loginDatalist[8][1])
        # 判断错误
        errText = self.loginPage.getElementValue(self.loginPage.errortext)
        # 弹窗提醒错误的信息
        try:
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("用户名或密码错误提示文本出现异常，异常是：%s" % e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("用户名或密码错误成功出现！")
            self.loginPage.doPhotos("_pass")
            sleep(1)
            # 弹窗确定按钮
            self.loginPage.doClick(self.loginPage.acceptBut)

    # 登录失败，用户名正确，密码长度不够
    def test_user_ok_pwd_short(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[9][0],
                                self.loginPage.loginDatalist[9][1])
        sleep(1)
        # #判断密码
        pwdText = self.loginPage.getElementValue(self.loginPage.errorpwd)
        try:
            self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("密码输入为空提示文本出现异常，异常是：%s" % e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("密码提示文本成功出现！")
            self.loginPage.doPhotos("_pass")

    # 登录失败，用户名正确，密码过长
    def test_user_ok_pwd_long(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[10][0],
                                self.loginPage.loginDatalist[11][1])
        sleep(1)
        # 判断错误
        errText = self.loginPage.getElementValue(self.loginPage.errortext)
        # 弹窗提醒错误的信息
        try:
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("用户名或密码错误提示文本出现异常，异常是：%s" % e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("用户名或密码错误成功出现！")
            self.loginPage.doPhotos("_pass")
            sleep(1)
            # 弹窗确定按钮
            self.loginPage.doClick(self.loginPage.acceptBut)

    # 登录失败，用户名过长，密码过长
    def test_user_long_pwd_long(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[11][0],
                                self.loginPage.loginDatalist[11][1])
        sleep(1)
        # 判断错误
        errText = self.loginPage.getElementValue(self.loginPage.errortext)
        # 弹窗提醒错误的信息
        try:
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("用户名或密码错误提示文本出现异常，异常是：%s" % e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("用户名或密码错误成功出现！")
            self.loginPage.doPhotos("_pass")
            sleep(1)
            # 弹窗确定按钮
            self.loginPage.doClick(self.loginPage.acceptBut)
    # 登录失败，用户过短，密码过短
    def test_user_short_pwd_short(self):
        self.loginPage.LoginFun(self.loginPage.loginDatalist[12][0],
                                self.loginPage.loginDatalist[12][1])
        sleep(1)
        #判断登录失败
        # #判断手机号
        nameText=self.loginPage.getElementValue(self.loginPage.erroruname)
        try:
            self.assertEqual("请输入手机号码", nameText)
        except Exception as e:
            log.logger.exception("请输入手机号码提示文本出现异常，异常是：%s" % e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("请输入手机号码文本提示成功出现！")
            self.loginPage.doPhotos("_pass")
        # #判断密码
        pwdText=self.loginPage.getElementValue(self.loginPage.errorpwd)
        try:
            self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("请输入6-20位账户密码提示文本出现异常，异常是：%s" % e, exc_info=True)
            self.loginPage.doPhotos("_faile")
        else:
            log.logger.info("请输入6-20位账户密码文本成功出现！")
            self.loginPage.doPhotos("_pass")




if __name__ == '__main__':
    unittest.main()


































































