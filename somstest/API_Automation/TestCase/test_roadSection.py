# -*- coding: utf-8 -*-
# @Time    : 2022-1-24
# @Author  : huangjing
# @File    : test_roadSection.py
# 使用009269的账号登录，进入路段管理，道路选择【青竹东路】，在该道路下添加路段。

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.roadSection_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestRoadSection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.roadSection = RoadSection_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【路段管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【路段管理】测试用例执行完毕')

    @logger("添加路段")
    def test_addRoadSection(self):
        """
            路段管理：添加路段
        """
        self.g["roadSectionName"] = "python青竹东路-" + str(random.randint(100, 999)) + "-路段"
        response = self.roadSection.add_roadSection(self.req_url, self.g["Cookie"],
                                                    roadSectionName=self.g["roadSectionName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询路段")
    def test_findRoadSection(self):
        """
            路段管理：查询路段
        """
        response = self.roadSection.find_roadSection(self.req_url, self.g["Cookie"])
        pythonRoadSection = response["body"]["rows"]
        for i in range(0, len(pythonRoadSection)):
            if pythonRoadSection[i]["roadSectionName"] == self.g["roadSectionName"]:
                self.g["roadSectionId"] = pythonRoadSection[i]["roadSectionId"]
        print(self.g["roadSectionId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["roadSectionName"])

    @logger("编辑路段")
    def test_editRoadSection(self):
        """
            路段管理：编辑路段
        """
        self.g["roadSectionName"] = "编辑" + self.g["roadSectionName"]
        response = self.roadSection.edit_roadSection(self.req_url, self.g["Cookie"],
                                                     roadSectionId=self.g["roadSectionId"],
                                                     roadSectionName=self.g["roadSectionName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除路段")
    def test_deleteRoadSection(self):
        """
            路段管理：删除路段
        """
        response = self.roadSection.delete_roadSection(self.req_url, self.g["Cookie"], self.g["roadSectionId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
