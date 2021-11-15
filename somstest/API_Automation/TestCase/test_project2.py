# -*- coding: utf-8 -*-
# @Time    : 2021-11-11
# @Author  : kuwanjun
# @File    : test_project2.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.project2_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestProject2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.project = Project2_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【项目管理（生产）】测试用例开始执行')

    def tearDown(self):
        LOG.info('【项目管理（生产）】测试用例执行完毕')

    @logger("添加项目（生产）")
    def test_addproject(self):
        """
            项目管理：添加销售项目
        """
        self.g["projectName"] = "python生产项目" + str(random.randint(100, 999))
        response = self.project.add_project(self.req_url, self.g["Cookie"], self.g["projectName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询项目（生产）")
    def test_findsproject(self):
        """
            项目管理：查询销售项目
        """
        response = self.project.finds_project(self.req_url, self.g["Cookie"])
        pythonproject = response["body"]["rows"]
        for i in range(0, len(pythonproject)):
            if pythonproject[i]["projectName"] == self.g["projectName"]:
                self.g["projectId"] = pythonproject[i]["projectId"]
        print("projectId:", self.g["projectId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("录入中标状态")
    def test_choiceproject(self):
        """
            项目管理：录入中标状态
        """

        response = self.project.choice_project(self.req_url, self.g["Cookie"], self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)


    @logger("查询项目（生产）")
    def test_findproject(self):
        """
            项目管理：查询生产项目
        """
        response = self.project.find_project(self.req_url, self.g["Cookie"])
        pythonproject = response["body"]["rows"]
        for i in range(0, len(pythonproject)):
            if pythonproject[i]["projectName"] == self.g["projectName"]:
                self.g["projectId"] = pythonproject[i]["projectId"]
        print("projectId:", self.g["projectId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑项目（生产）")
    def test_editproject(self):
        """
            项目管理：编辑生产项目
        """
        self.g["projectName"] = "编辑" + self.g["projectName"]
        response = self.project.edit_project(self.req_url, self.g["Cookie"], self.g["projectId"],
                                       self.g["projectName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("选中项目")
    def test_findxsroad(self):
        """
            道路管理：选中生产项目
        """
        response = self.project.findxs_road(self.req_url, self.g["Cookie"], self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'total', 0)

    @logger("添加道路（生产）")
    def test_addroad(self):
        """
            道路管理：添加生产道路
        """
        self.g["roadName"] = "python生产道路" + str(random.randint(100, 999))
        response = self.project.add_road(self.req_url, self.g["Cookie"], self.g["roadName"],
                                         self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)


    @logger("查询道路（生产）")
    def test_findroad(self):
        """
            道路管理：查询生产道路
        """
        response = self.project.find_road(self.req_url, self.g["Cookie"], self.g["projectId"])
        pythonroad = response["body"]["rows"]
        for i in range(0, len(pythonroad)):
            if pythonroad[i]["roadName"] == self.g["roadName"]:
                self.g["roadId"] = pythonroad[i]["roadId"]
        print("roadId:", self.g["roadId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑道路（生产）")
    def test_editroad(self):
        """
            道路管理：编辑生产道路
        """
        self.g["roadName"] = "编辑" + self.g["roadName"]
        response = self.project.edit_road(self.req_url, self.g["Cookie"], self.g["roadId"],
                                          self.g["roadName"], self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除道路（生产）")
    def test_deleteroad(self):
        """
            道路管理：删除生产道路
        """
        response = self.project.delete_road(self.req_url, self.g["Cookie"], self.g["roadId"],
                                            self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除项目（生产）")
    def test_deleteproject(self):
        """
            项目管理：删除生产项目
        """
        response = self.project.delete_project(self.req_url, self.g["Cookie"], self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
