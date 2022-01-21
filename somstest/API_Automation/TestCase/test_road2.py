# -*- coding: utf-8 -*-
# @Time    : 2022-1-21
# @Author  : huangjing
# @File    : test_road2.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.road2_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestRoad2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.road = Road2_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【道路管理（生产）】测试用例开始执行')

    def tearDown(self):
        LOG.info('【道路管理（生产）】测试用例执行完毕')

    @logger("添加道路（生产）")
    def test_addroad(self):
        """
            道路管理(生产)：添加道路
        """
        # 在【大竹林项目】下添加道路
        self.g["roadName"] = "python道路" + str(random.randint(100, 999))
        response = self.road.add_road(self.req_url, self.g["Cookie"], self.g["roadName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询道路（生产）")
    def test_findroad(self):
        """
            道路管理(生产)：查询道路
        """
        response = self.road.find_road(self.req_url, self.g["Cookie"], searchValue=self.g["roadName"])
        pythonroad = response["body"]["rows"]
        for i in range(0, len(pythonroad)):
            if pythonroad[i]["roadName"] == self.g["roadName"]:
                self.g["roadId"] = pythonroad[i]["roadId"]
        print("roadId:", self.g["roadId"])
        assert self.initEvn.test.assert_in_text(response["body"], self.g["roadName"])

    @logger("指派踏勘人")
    def test_saveExplorer(self):
        """
            道路管理(生产)：指派踏勘人
        """
        response = self.road.add_road(self.req_url, self.g["Cookie"], self.g["roadId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("编辑道路（生产）")
    def test_editroad(self):
        """
            道路管理(生产)：编辑道路
        """
        self.g["roadName"] = "编辑" + self.g["roadName"]
        response = self.road.edit_road(self.req_url, self.g["Cookie"], self.g["roadId"],
                                       self.g["roadName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除道路（生产）")
    def test_deleteroad(self):
        """
            道路管理(生产)：删除道路
        """
        response = self.road.delete_road(self.req_url, self.g["Cookie"], self.g["roadId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
