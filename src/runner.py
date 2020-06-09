#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import pytest
import subprocess
import os

fileHandler = logging.FileHandler(filename="../log/auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':
    #print(os.getcwd())
    logging.info("Start to execute  automation cases")
    # 执行test指定某个测试用例，可调试用
    # pytest.main(['-sq', '--cache-clear', '--disable-warnings', '--alluredir', '../log/testreport/xml',
    #              'testcases/contact/depmanagement/test_dep_lists.py'])

    # 执行testcase下所有用例
        pytest.main(['-sq', '--cache-clear', '--disable-warnings', '--alluredir', '../log/testreport/xml',
                 'testcases'])

    # 执行testcase下带指定标签的测试用例
    #pytest.main(['-sq', '--cache-clear', '--disable-warnings', '--alluredir', '../log/testreport/xml',
    #           '-m', 'Success'])
    # 生成html的测试报告
    print(subprocess.getstatusoutput('allure generate --clean ../log/testreport/xml -o ../log/testreport/html'))

    logging.info("End to execute  automaction cases")
