# -*- coding: utf-8 -*-
# @Time    : 2021-11-8
# @Author  : kuwanjun
# @File    : test_road1.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.road1_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestRoad1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.road = Road1_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_adminCookie()

        LOG.info('【道路管理（销售）】测试用例开始执行')

    def tearDown(self):
        LOG.info('【道路管理（销售）】测试用例执行完毕')

    @logger("选中项目")
    def test_findxsroad(self):
        """
            道路管理（销售）：选中项目（销售）
        """
        response = self.road.findxs_road(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], "两江新区")

    @logger("添加道路")
    def test_addroad(self):
        """
            道路管理（销售）：添加道路（销售）
        """
        self.g["roadName"] = "python道路" + str(random.randint(100, 999))
        response = self.road.add_road(self.req_url, self.g["Cookie"], self.g["roadName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询道路")
    def test_findroad(self):
        """
            道路管理（销售）：查询道路（销售）
        """
        response = self.road.find_road(self.req_url, self.g["Cookie"])
        pythonroad = response["body"]["rows"]
        for i in range(0, len(pythonroad)):
            if pythonroad[i]["roadName"] == self.g["roadName"]:
                self.g["roadId"] = pythonroad[i]["roadId"]
        print("roadId:", self.g["roadId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")


    @logger("编辑道路")
    def test_editroad(self):
        """
            道路管理（销售）：编辑道路（销售）
        """
        self.g["roadName"] = "编辑" + self.g["roadName"]
        response = self.road.edit_road(self.req_url, self.g["Cookie"], self.g["roadId"],
                                       self.g["roadName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("指派踏勘人")
    def test_Explorerroad(self):
        """
            道路管理（销售）：指派踏勘人
        """
        response = self.road.Explorer_road(self.req_url, self.g["Cookie"], self.g["roadId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除道路")
    def test_deleteroad(self):
        """
            道路管理（销售）：删除道路（销售）
        """
        response = self.road.delete_road(self.req_url, self.g["Cookie"], self.g["roadId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
