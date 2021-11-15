# -*- coding: utf-8 -*-
# @Time    : 2021-11-10
# @Author  : huangjing
# @File    : test_project4.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.project4_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestProject4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.project = Project4_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【收运项目管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【收运项目管理】测试用例执行完毕')

    @logger("添加项目")
    def test_addProject(self):
        """
            项目管理：添加项目
        """
        self.g["projectName"] = "python收运项目" + str(random.randint(100, 999))
        response = self.project.add_project(self.req_url, self.g["Cookie"], projectName=self.g["projectName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询项目")
    def test_findProject(self):
        """
            项目管理：查询项目
        """
        response = self.project.find_project(self.req_url, self.g["Cookie"])
        pythonproject = response["body"]["rows"]
        for i in range(0, len(pythonproject)):
            if pythonproject[i]["projectName"] == self.g["projectName"]:
                self.g["projectId"] = pythonproject[i]["projectId"]
        print("projectId:", self.g["projectId"])
        assert self.initEvn.test.assert_in_text(response["body"], self.g["projectName"])

    @logger("编辑项目")
    def test_editProject(self):
        """
            项目管理：编辑项目
        """
        self.g["projectName"] = "编辑" + self.g["projectName"]
        response = self.project.edit_project(self.req_url, self.g["Cookie"], projectId=self.g["projectId"],
                                             projectName=self.g["projectName"])
        assert self.initEvn.test.assert_body(response["body"], 'resultCode', 1)

    @logger("删除项目")
    def test_deleteProject(self):
        """
            项目管理：删除项目
        """
        response = self.project.delete_project(self.req_url, self.g["Cookie"], projectId=self.g["projectId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
