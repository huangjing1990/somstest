# -*- coding: utf-8 -*-
# @Time    : 2021-9-28
# @Author  : huangjing
# @File    : test_patrolItems.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.patrolItems_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestPatrolItems(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.item = PatrolItems_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【巡查项管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【巡查项管理】测试用例执行完毕')

    @logger("添加检查类")
    def test_addParentItem(self):
        """
            巡查项管理：添加检查类
        """
        # self.g["operationItemName"]
        self.g["parentItemName"] = "python检查类" + str(random.randint(100, 999))
        response = self.item.add_patrolItem(self.req_url, self.g["Cookie"], parentItemId=None,
                                            operationItemName=self.g["parentItemName"], itemType="0")
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询检查类")
    def test_findParentItem(self):
        """
            巡查项管理：查询检查类
        """
        response = self.item.find_patrolItem(self.req_url, self.g["Cookie"])
        pythondata = response["body"]["rows"]
        for i in range(0, len(pythondata)):
            if pythondata[i]["operationItemName"] == self.g["parentItemName"]:
                self.g["parentItemId"] = pythondata[i]["operationItemId"]
        print("parentItemId: ", self.g["parentItemId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["parentItemName"])

    @logger("添加检查项")
    def test_addOperationItem(self):
        """
            巡查项管理：添加检查项
        """
        self.g["operationItemName"] = "python检查项" + str(random.randint(100, 999))
        response = self.item.add_patrolItem(self.req_url, self.g["Cookie"], parentItemId=self.g["parentItemId"],
                                            operationItemName=self.g["operationItemName"], itemType="1")
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询检查项")
    def test_findOperationItem(self):
        """
            巡查项管理：查询检查项
        """
        response = self.item.find_patrolItem(self.req_url, self.g["Cookie"])
        pythondata = response["body"]["rows"]
        for i in range(0, len(pythondata)):
            if pythondata[i]["operationItemName"] == self.g["parentItemName"]:
                operationdata = pythondata[i]["children"]
                for j in range(0, len(operationdata)):
                    if operationdata[j]["operationItemName"] == self.g["operationItemName"]:
                        self.g["operationItemId"] = operationdata[j]["operationItemId"]
        print("operationItemId: ", self.g["operationItemId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["operationItemName"])

    @logger("编辑检查项")
    def test_editOperationItem(self):
        """
            巡查项管理：编辑检查项
        """
        # itemType:0 检查类；1检查项
        self.g["operationItemName"] = "编辑" + self.g["operationItemName"]
        response = self.item.edit_patrolItem(self.req_url, self.g["Cookie"], parentItemId=self.g["parentItemId"],
                                             operationItemId=self.g["operationItemId"],
                                             operationItemName=self.g["operationItemName"],
                                             itemType="1")
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("编辑检查类")
    def test_editParentItem(self):
        """
            巡查项管理：编辑检查类
        """
        # itemType:0 检查类；1检查项
        self.g["parentItemName"] = "编辑" + self.g["parentItemName"]
        response = self.item.edit_patrolItem(self.req_url, self.g["Cookie"], parentItemId=None,
                                             operationItemId=self.g["parentItemId"],
                                             operationItemName=self.g["parentItemName"],
                                             itemType="0")
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("刷新")
    def test_refresh(self):
        """
            巡查项管理：刷新
        """
        response = self.item.find_patrolItem(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["parentItemName"])

    @logger("删除检查项")
    def test_deleteOperationItem(self):
        """
            巡查项管理：删除检查项
        """
        response = self.item.delete_patrolItem(self.req_url, self.g["Cookie"], self.g["operationItemId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除检查类")
    def test_deleteParentItem(self):
        """
            巡查项管理：删除检查类
        """
        response = self.item.delete_patrolItem(self.req_url, self.g["Cookie"], self.g["parentItemId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
