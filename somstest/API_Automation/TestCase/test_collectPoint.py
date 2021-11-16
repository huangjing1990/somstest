# -*- coding: utf-8 -*-
# @Time    : 2021-11-16
# @Author  : huangjing
# @File    : test_collectPoint.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.collectPoint_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestCollectPoint(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.collect = CollectPoint_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【收运点管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【收运点管理】测试用例执行完毕')

    @logger("查询所有公共类收运点")
    def test_findCollectPoint(self):
        """
            收运点管理：查询所有公共类收运点
        """
        response = self.collect.find_collectPoint(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], "大竹林")

    @logger("根据名称查找收运点")
    def test_findCollectPointByName(self):
        """
            收运点管理：根据名称查找收运点
        """
        response = self.collect.find_collectPointByName(self.req_url, self.g["Cookie"])
        pythoncollect = response["body"]
        for i in range(0, len(pythoncollect)):
            if pythoncollect[i]["pointName"] == "大竹林":
                self.g["collectorPointId"] = pythoncollect[i]["pointId"]
        print("collectorPointId:", self.g["collectorPointId"])
        assert self.initEvn.test.assert_in_text(response["body"], "大竹林")

    @logger("查看收运点详情")
    def test_lookCollectPoint(self):
        """
            收运点管理：查看收运点详情
        """
        response = self.collect.look_collectPoint(self.req_url, self.g["Cookie"],
                                                  collectorPointId=self.g["collectorPointId"])
        assert self.initEvn.test.assert_in_text(response["body"], "大竹林")

    @logger("编辑收运点")
    def test_editCollectPoint(self):
        """
            收运点管理：编辑收运点
        """
        response = self.collect.edit_collectPoint(self.req_url, self.g["Cookie"],
                                                  collectorPointId=self.g["collectorPointId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
