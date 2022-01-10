# -*- coding: utf-8 -*-
# @Time    : 2021-11-18
# @Author  : kuwanjun
# @File    : test_road3.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.road3_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestRoad3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.road = Road3_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_adminCookie()

        LOG.info('【人工道路管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【人工道路管理】测试用例执行完毕')

    @logger("添加人工道路")
    def test_addroad(self):
        """
            道路管理：添加人工道路
        """
        self.g["roadName"] = "python人工道路" + str(random.randint(100, 999))
        response = self.road.add_road(self.req_url, self.g["Cookie"], self.g["roadName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询人工道路")
    def test_findroad(self):
        """
            道路管理：查询人工道路
        """
        response = self.road.find_road(self.req_url, self.g["Cookie"])
        pythonroad = response["body"]["rows"]
        for i in range(0, len(pythonroad)):
            if pythonroad[i]["roadName"] == self.g["roadName"]:
                self.g["roadId"] = pythonroad[i]["roadId"]
        print("roadId:", self.g["roadId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑人工道路")
    def test_editroad(self):
        """
            道路管理：编辑人工道路
        """
        self.g["roadName"] = "编辑" + self.g["roadName"]
        response = self.road.edit_road(self.req_url, self.g["Cookie"], self.g["roadId"],
                                       self.g["roadName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除人工道路")
    def test_deleteroad(self):
        """
            道路管理：删除人工道路
        """
        response = self.road.delete_road(self.req_url, self.g["Cookie"], self.g["roadId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
