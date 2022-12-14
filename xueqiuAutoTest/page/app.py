from appium import webdriver

from page.BasePage import BasePage
from page.main import Main

class APP(BasePage):
    def start(self):
        _APPPackage="com.xueqiu.android"
        _ApppActivity=".view.WelcomeActivityAlias"
        if self._driver is None:
            caps={}
            caps['platformName']='Android'
            caps['platformVersion']='7.1.2'
            caps['deviceName']='127.0.0.1:62001'
            caps['app']='C:\\Users\\17201\\Desktop\\xueqiu.apk'
            caps['noReset']=True
            caps['appPackage']=_APPPackage
            caps['appWaitActivity']=_ApppActivity
            self._driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
            self._driver.implicitly_wait(20)
        else:
            #启动页面
            self._driver.start_activity(_APPPackage,_ApppActivity)

        return self
    def main(self):
        return Main(self._driver)
