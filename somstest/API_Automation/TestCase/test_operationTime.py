# -*- coding: utf-8 -*-
# @Time    : 2021-8-20
# @Author  : huangjing
# @File    : test_operationTime.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.operationTime_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestOperationTasks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.time = OperationTime_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加时段")
    def test_addtime(self):
        """
            时段管理：添加时段
        """
        response = self.time.add_time(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询时段")
    def test_findtime(self):
        """
            时段管理：查询时段
        """
        response = self.time.find_time(self.req_url, self.g["Cookie"])
        pythontask = response["body"]["rows"]
        for i in range(0, len(pythontask)):
            if pythontask[i]["operationTimeName"] == "python时段":
                self.g["operationTimeId"] = pythontask[i]["operationTimeId"]
        print("operationTimeId:", self.g["operationTimeId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑时段")
    def test_edittime(self):
        """
            时段管理：编辑时段
        """
        response = self.time.edit_time(self.req_url, self.g["Cookie"], self.g["operationTimeId"])
        assert self.initEvn.test.assert_body(response["body"], 'resultCode', 1)

    @logger("删除时段")
    def test_deletetime(self):
        """
            时段管理：删除时段
        """
        response = self.time.delete_time(self.req_url, self.g["Cookie"], self.g["operationTimeId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
