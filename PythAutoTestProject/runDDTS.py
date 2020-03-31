import unittest
import time
from ToolsFile import HTMLTestReportEN


class FuncTest(unittest.TestCase):

    def runFunVerify_1001(self):
        # TODO: finish the method contract context
        h = 8+ 8
        self.assertEqual(h,17,'runFunVerify_1002')

def Suite():
    '''
    () -> suite object
    Return the suite object which stored the test cases suite declared in test classes.
    '''
    suite = unittest.TestSuite()
    suite.addTest(FuncTest('runFunVerify_1001'))
    return suite
if __name__ == '__main__':
    filename = 'test.html'
    #定义报告文件权限，wb，表示有读写权限
    fp = open(filename,'wb')
    runner = HTMLTestReportEN.HTMLTestRunner(
        stream=fp,
        title='The testing report for ...',
        description='This is our auto testing result summary.')
    # 执行测试
    runner.run(Suite())

    # 关闭文件，否则会无法生成文件
    time.sleep(2)
    fp.close()