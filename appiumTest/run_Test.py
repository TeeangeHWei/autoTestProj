#coding=utf-8
import unittest,os,time
import HTMLTestRunner

cur_Path = os.path.dirname(os.path.realpath(__file__))
case_Path = os.path.join(cur_Path,'testcases')
report_path = os.path.join(cur_Path,'reports')

if __name__ == '__main__':
    #加载用例方法
    testlist = unittest.defaultTestLoader.discover(case_Path,pattern='login*.py')
    #当前时间
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    report_name = report_path + '\\' + now_time + 'result.html'
    fp = HTMLTestRunner.HTMLTestRunner(stream=open(report_name,'wb'),title='appium-yamimeal',description='win10')
    print(testlist)
    fp.run(testlist)






