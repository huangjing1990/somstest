# -*- coding: utf-8 -*-
# @Time    : 2021-9-29
# @Author  : huangjing
# @File    : test_patrolStandard.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.patrolStandard_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestPatrolStandard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.standard = PatrolStandard_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加评分标准")
    def test_addParentStandard(self):
        """
            巡查评分标准：添加评分标准
        """
        self.g["operationLevelName"] = "python评分标准" + str(random.randint(100, 999))
        response = self.standard.add_patrolStandard(self.req_url, self.g["Cookie"],
                                                    operationLevelName=self.g["operationLevelName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询评分标准")
    def test_findParentStandard(self):
        """
            巡查评分标准：查询评分标准
        """
        response = self.standard.find_patrolStandard(self.req_url, self.g["Cookie"],
                                                     operationLevelName=self.g["operationLevelName"])
        pythondata = response["body"]["rows"]
        for i in range(0, len(pythondata)):
            if pythondata[i]["operationLevelName"] == self.g["operationLevelName"]:
                self.g["operationLevelId"] = pythondata[i]["operationLevelId"]
        print("operationLevelId: ", self.g["operationLevelId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["operationLevelName"])

    @logger("编辑评分标准")
    def test_editParentStandard(self):
        """
            巡查评分标准：编辑评分标准
        """
        self.g["operationLevelName"] = "编辑" + self.g["operationLevelName"]
        response = self.standard.edit_patrolStandard(self.req_url, self.g["Cookie"],
                                                     operationLevelId=self.g["operationLevelId"],
                                                     operationLevelName=self.g["operationLevelName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 2)

    @logger("查看")
    def test_findParentStandardById(self):
        """
            巡查评分标准：查看
        """
        response = self.standard.find_patrolStandardById(self.req_url, self.g["Cookie"],
                                                         operationLevelId=self.g["operationLevelId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["operationLevelName"])

    @logger("选择时段")
    def test_chooseOperationTime(self):
        """
            巡查评分标准：选择时段
        """
        response = self.standard.chooseOperationTime(self.req_url, self.g["Cookie"],
                                                     operationLevelId=self.g["operationLevelId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除评分标准")
    def test_deleteParentStandard(self):
        """
            巡查评分标准：删除评分标准
        """
        response = self.standard.delete_patrolStandard(self.req_url, self.g["Cookie"],
                                                       operationLevelId=self.g["operationLevelId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
