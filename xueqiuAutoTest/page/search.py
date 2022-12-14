import time

from page.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By
class Search(BasePage):
    def searchinput(self,key):
        self.find(By.ID,"search_input_text").send_keys(key)
        time.sleep(5)
        self.find(By.ID,"name").click()
        time.sleep(3)
        return self
    def get_price(self):
        return float(self.find(By.ID,"com.xueqiu.android:id/current_price").text)


