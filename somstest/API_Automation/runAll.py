#!/usr/bin/
# -*- coding: UTF-8 -*-

import unittest
from Common.log_Common import *
import time
from Common.file_utils import *
from BeautifulReport import BeautifulReport
from ut.core import _TestCase

caseList = []
proDir = os.path.split(os.path.realpath(__file__))[0]


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


def set_case_list(testFile_path):
    fb = open(testFile_path)
    for value in fb.readlines():
        data = str(value)
        if data != '' and not data.startswith("#"):
            caseList.append(data.replace("\n", ""))
    fb.close()


def creat_suite(testcase_path):
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test_*.py', top_level_dir=None)
    return discover


def set_case_suite(testFile_path):
    set_case_list(testFile_path)
    test_suite = unittest.TestSuite()
    suite_model = []
    for case in caseList:
        case_file = os.path.join(proDir, "TestCase")
        LOG.info(case_file)
        case_name = case.split("/")[-1]
        LOG.info(case_name + ".py")
        discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
        LOG.info(discover)
        suite_model.append(discover)

    if len(suite_model) > 0:
        for suite in suite_model:
            for test_name in suite:
                test_suite.addTest(test_name)
    else:
        return None
    return test_suite


def runs(testFile_path):
    try:
        suit = set_case_suite(testFile_path)
        if suit is not None:
            LOG.info("********TEST START********")
            fp = open(get_report_path(), 'wb')
            current_path = os.getcwd()
            report_path = os.path.join(current_path, "report")
            run = BeautifulReport(suit)
            run.report(description="迅洁智慧环卫系统", tester="黄静", filename="接口自动化测试", log_path=report_path)
        else:
            LOG.info("Have no case to test.")
    except Exception as ex:
        LOG.info(str(ex))
    finally:
        LOG.info("*********TEST END*********")


if __name__ == '__main__':
    delete_log()
    unittest.TestCase = _TestCase
    testFile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "testFile"))
    suite = runs(testFile_path + "\\caselist.txt")
