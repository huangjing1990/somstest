# -*- coding: utf-8 -*-
# @Time    : 2021-10-09
# @Author  : huangjing
# @File    : test_fence.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.fence_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestFence(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.fence = Fence_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加电子围栏")
    def test_addFence(self):
        """
            电子围栏：添加电子围栏
        """
        self.g["fenceName"] = "python电子围栏" + str(random.randint(100, 999))
        response = self.fence.add_fence(self.req_url, self.g["Cookie"], self.g["fenceName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查看电子围栏")
    def test_findFence(self):
        """
            电子围栏：查看电子围栏
        """
        response = self.fence.find_fence(self.req_url, self.g["Cookie"])
        fencedata = response["body"]["rows"]
        for i in range(0, len(fencedata)):
            if fencedata[i]["fenceName"] == self.g["fenceName"]:
                self.g["fenceId"] = fencedata[i]["fenceId"]
        print("fenceId: ", self.g["fenceId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["fenceName"])

    @logger("选择车辆")
    def test_chooseVehicle(self):
        """
            电子围栏：选择车辆
        """
        response = self.fence.choose_vehicle(self.req_url, self.g["Cookie"], self.g["fenceId"])
        assert self.initEvn.test.assert_in_text(response['body'], "选择成功")

    @logger("编辑电子围栏")
    def test_editFence(self):
        """
            电子围栏：编辑电子围栏
        """
        self.g["fenceName"] = "编辑" + self.g["fenceName"]
        response = self.fence.edit_fence(self.req_url, self.g["Cookie"], fenceId=self.g["fenceId"],
                                         fenceName=self.g["fenceName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除电子围栏")
    def test_deleteFence(self):
        """
            电子围栏：删除电子围栏
        """
        response = self.fence.delete_fence(self.req_url, self.g["Cookie"], self.g["fenceId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
