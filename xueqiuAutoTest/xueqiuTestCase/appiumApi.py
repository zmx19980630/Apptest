import time

from appium import webdriver

_APPPackage = "com.xueqiu.android"
_ApppActivity = ".view.WelcomeActivityAlias"
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
caps['deviceName'] = '127.0.0.1:62001'
caps['app'] = 'C:\\Users\\17201\\Desktop\\xueqiu.apk'
caps['noReset'] = True
caps['appPackage'] = _APPPackage
caps['appWaitActivity'] = _ApppActivity
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(20)
#关闭app
driver.close_app()
#确认是否安装软件
driver.is_app_installed(_APPPackage)
#卸载app
driver.remove_app(_APPPackage)
time.sleep(3)

#安装app
driver.install_app("")
time.sleep(3)

#打开指定页面
driver.start_activity(_APPPackage,_ApppActivity)
time.sleep(3)

#置后台
driver.background_app(5)
time.sleep(3)
#重置
driver.reset()
#操作键码表
driver.press_keycode(26)
#手势类操作，滑动，长按，拖拽
from  appium.webdriver.common.touch_action import TouchAction
#按压控件，或坐标点二选一，即不能填写两个
#release()结束动作，释放按压指针,perform()执行
TouchAction(driver).press([200,300]).release().perform()
#长按先执行，后释放
element=driver.find_element("")
TouchAction(driver).long_press(element).perform().release()
# 点击,注意：语法列表套元组-[(x,y)]第一种：内置tap函数、第二种：使用TouchAction类
driver.tap([(100,200)])
TouchAction(driver).tap(element=None).perform().release()
# 暂停,单位是毫秒
TouchAction(driver).wait(2000)
# 移动,element目标位置元素
TouchAction(driver).move_to(element).perform().release()
TouchAction(driver).long_press().move_to().perform().release()
# 滑动
driver.swipe(200,300,300,200,times)
# 收起键盘
driver.hide_keyboard()
# 摇一摇
driver.shake()
# 滚动，从a元素到b元素
A_element=driver.find_element()
B_element=driver.find_element()
driver.scroll(A_element,B_element)
driver.flick(200,300,300,200)
#放大、缩小
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
action1=TouchAction(driver)
action2=TouchAction(driver)
zoom=MultiAction(driver)
action1.press(200,300).wait(1000).move_to(300,200).wait(1000)
action2.press(100,200).wait(1000).move_to(300,200).wait(1000)
zoom.add(action1,action2)
#获取屏幕分辨率(宽、高)
x=driver.get_window_size()['width']
y=driver.get_window_size()['height']
driver.swipe(0.8*x,0.5*y,0.2*x,0.1*y,2000)
