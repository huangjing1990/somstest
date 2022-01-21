# -*- coding: utf-8 -*-
# @Time    : 2022-1-13
# @Author  : huangjing
# @File    : test_project2.py
# 项目管理（生产）的编辑、删除和查询功能。

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

    @logger("查询项目（生产）")
    def test_findproject(self):
        """
            项目管理：查询项目（生产）
        """
        response = self.project.find_project(self.req_url, self.g["Cookie"])
        pythonproject = response["body"]["rows"]
        for i in range(0, len(pythonproject)):
            if pythonproject[i]["projectName"] == "大竹林项目":
                self.g["projectId"] = pythonproject[i]["projectId"]
        print("projectId:", self.g["projectId"])
        assert self.initEvn.test.assert_in_text(response["body"], "大竹林项目")

    @logger("编辑项目（生产）")
    def test_editorg(self):
        """
            项目管理：编辑项目（生产）
        """
        response = self.project.update_project(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
