# -*- coding: utf-8 -*-
# @Time    : 2022-1-27
# @Author  : huangjing
# @File    : test_cleanRoute.py
# 苏丽芳213492登录系统，进行收运路线的增删改查。部门id=1557，项目id=1276，收运点id=5570;5592;5594;5569;

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.cleanRoute_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestCleanRoute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.cleanRoute = CleanRoute_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_user1Cookie()

        LOG.info('【收运路线】测试用例开始执行')

    def tearDown(self):
        LOG.info('【收运路线】测试用例执行完毕')

    @logger("添加收运路线")
    def test_addCleanRoute(self):
        """
            收运路线：添加收运路线
        """
        self.g["cleanRouteName"] = "python收运路线" + str(random.randint(100, 999))
        response = self.cleanRoute.add_cleanRoute(self.req_url, self.g["Cookie"],
                                                  cleanRouteName=self.g["cleanRouteName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询收运路线")
    def test_findCleanRoute(self):
        """
            收运路线：查询收运路线
        """
        response = self.cleanRoute.find_cleanRoute(self.req_url, self.g["Cookie"])
        pythonRoute = response["body"]["rows"]
        for i in range(0, len(pythonRoute)):
            if pythonRoute[i]["routeName"] == self.g["cleanRouteName"]:
                self.g["cleanRouteId"] = pythonRoute[i]["routeId"]
        assert self.initEvn.test.assert_in_text(response['body'], self.g["cleanRouteName"])

    @logger("编辑收运路线")
    def test_editCleanRoute(self):
        """
            收运路线：编辑收运路线
        """
        self.g["cleanRouteName"] = "编辑" + self.g["cleanRouteName"]
        response = self.cleanRoute.edit_cleanRoute(self.req_url, self.g["Cookie"], cleanRouteId=self.g["cleanRouteId"],
                                                   cleanRouteName=self.g["cleanRouteName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("禁用收运路线")
    def test_disableCleanRoute(self):
        """
            收运路线：禁用收运路线
        """
        response = self.cleanRoute.disable_cleanRoute(self.req_url, self.g["Cookie"], self.g["cleanRouteId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除收运路线")
    def test_deleteCleanRoute(self):
        """
            收运路线：删除收运路线
        """
        response = self.cleanRoute.delete_cleanRoute(self.req_url, self.g["Cookie"], self.g["cleanRouteId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
