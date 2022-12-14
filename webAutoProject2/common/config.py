#conding="utf-8"
#所有的配置文件的信息
#基本的页面地址
import os
import time

base_url="http://139.199.0.102/passport/login"
#项目地址+截图地址
base_path=r"D:\pythonCoding\webAutoProject2\\"
# photo_path=base_path+"/data/photos/"
photo_path=os.path.join(base_path,r"data\photos\\")
#当前时间，格式化时间
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")
#当前日期
cur_date=time.strftime("%Y_%m_%d")
#log路径
# log_path=base_path+"/data/logs/"
log_path=os.path.join(base_path,r"data\logs\\")
#excel的路径
data_path=os.path.join(base_path,r"data\testDatas\\")
#测试用例路径
test_path=os.path.join(base_path,r"demo\testCase\\")
#测试报告路径
report_path=os.path.join(base_path,r"data\reports\\")






















