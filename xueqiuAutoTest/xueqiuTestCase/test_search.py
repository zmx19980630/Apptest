import os

import allure
import pytest,yaml
from page.app import APP
@allure.feature("搜索模块")
class TestSearch:
    @pytest.mark.parametrize("key,price",
                             yaml.safe_load(
                                 open("D:\\pythonCoding\\xueqiuAutoTest\\Testdata\\researchdata.yml")))
    @allure.story("搜索框搜索公司股价")
    def test_search001(self,key,price):
        with allure.step("1、首页点击搜索，进入搜索页面2、输入关键词进行搜索，并断言"):
            assert APP().start().main().goto_search_page()\
                   .searchinput(key).get_price()>float(price)
    @allure.story("点击头像进入我的页面")
    def test_photo001(self):
        APP().start().main().goto_my_photo()
# if __name__ == '__main__':
    # pytest.main(['./xueqiuTestCase/test_search.py','-sv',"--alluredir","../Testreport/report"])
    # os.system("allure generate ../Testreport/report -o ../Testreport/report --clean")



































