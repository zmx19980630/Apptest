#coding="utf-8"
# #搜索郑州市人民政府，点击新闻中心
# from time import sleep
#
# from selenium import webdriver
#
# #实例化浏览器，打开页面
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com/")
# driver.maximize_window()
# sleep(1)
# #定位输入框，并输入“郑州市人民政府”
# inp=driver.find_element_by_id("kw")
# inp.send_keys("郑州市人民政府")
# sleep(1)
# #点击百度一下
# driver.find_element_by_id("su").click()
# sleep(1)
# #点击人民政府
# zf=driver.find_element_by_link_text("郑州市人民政府")
# zf.click()
# sleep(1)
# #转移句柄到郑州市人民政府首页
# handels=driver.window_handles
# driver.switch_to.window(handels[1])
# sleep(2)
# #定位新闻中心并点击新闻中心
# driver.find_element_by_xpath("//a[@title='新闻中心']").click()
# sleep(3)
# driver.quit()
# import random
# while True:
#     a = int(input("请输入您要猜的数字："))
#     num = random.randrange(1, 10)
#     if a>num:
#         print("猜错了，数字猜大了")
#     elif a<num:
#         print("猜错了，数字猜小了")
#     else:
#         print("恭喜您，猜对了")
#         break
# a=int(input("请输入数字："))
# arr=[0]*a
# for i in arr:
#     print("hello")
a = int(input("请输入数字："))
print("hello\n"*a)
