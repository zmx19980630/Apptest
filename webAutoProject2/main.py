import unittest

from common import doSuite, doReport

if __name__ == '__main__':
    #获取测试套件
    # suite=unittest.TestSuite()
    # suite=doSuite.addTestByMethon(suite)
    #不需要第一步的实例化unnitest.TestSuite对象，会自动生成一个
    suite1=doSuite.addTestByAuto()
    #执行测试套件，并生成测试报告
    # run=unittest.TextTestRunner()
    # run.run(suite)
    #执行测试套件，并生成txt版本的测试报告
    # doReport.doTextReport(suite)
    # 执行测试套件，并生成HTML版本的测试报告
    # doReport.doHTMLReport(suite)
    # 执行测试套件，并生成更完美的HTML版本的测试报告
    doReport.doHTMLReport_more(suite1)










































