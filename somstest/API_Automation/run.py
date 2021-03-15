#!/usr/bin/
# -*- coding: UTF-8 -*-

import HTMLTestRunner
import unittest
from Common.log_Common import *
from Common.file_utils import *
import os
import time
from ut.core import _TestCase


def creat_suite(testcase_path):
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test_*.py', top_level_dir=None)
    return discover


# 判断log文件夹是否存在，不存在新建，存在的话删除里面的文件
def delete_log():
    log_dir = os.path.join(os.getcwd(), "Log")
    print(log_dir)
    isLogDirExists = os.path.exists(log_dir)
    if isLogDirExists:
        delete_file(log_dir)
    else:
        os.makedirs(log_dir)
    LOG.info("日志路径; %s" % log_dir)


# 判断报告文件夹是否存在，不存在新建，存在的话删除里面的文件
def get_report_path():
    report_dir = os.path.join(os.getcwd(), "report")
    isReportDirExists = os.path.exists(report_dir)
    if isReportDirExists:
        delete_file(report_dir)
    else:
        os.makedirs(report_dir)
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    report_path = report_dir + "\\report_" + now + ".html"
    LOG.info("报告路径; %s" % report_path)
    return report_path


if __name__ == '__main__':
    unittest.TestCase = _TestCase
    testcase_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "TestCase"))
    delete_log()
    suite = creat_suite(testcase_path)
    fp = open(get_report_path(), "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="自动化测试结果",
                                           verbosity=2)
    runner.run(suite)
    fp.close()
