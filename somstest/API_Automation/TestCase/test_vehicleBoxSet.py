# -*- coding: utf-8 -*-
# @Time    : 2021-10-22
# @Author  : kuwanjun
# @File    : test_vehicleBoxSet.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.vehicleBoxSet_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestVehicleBoxSet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.vehicleBoxSet = VehicleBoxSet_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【油水箱设置】测试用例开始执行')

    def tearDown(self):
        LOG.info('【油水箱设置】测试用例执行完毕')

    @logger("添加油水箱")
    def test_addvehicleBoxSet(self):
        """
            油水箱设置：添加油水箱
        """
        self.g["name"] = "python油水箱" + str(random.randint(100, 999))
        response = self.vehicleBoxSet.add_vehicleBoxSet(self.req_url, self.g["Cookie"], self.g["name"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询油水箱")
    def test_findvehicleBoxSet(self):
        """
            油水箱设置：查询油水箱
        """
        response = self.vehicleBoxSet.find_vehicleBoxSet(self.req_url, self.g["Cookie"])
        pythonvehicleBoxSet = response["body"]["rows"]
        for i in range(0, len(pythonvehicleBoxSet)):
            if pythonvehicleBoxSet[i]["name"] == self.g["name"]:
                self.g["vehicleBoxSetId"] = pythonvehicleBoxSet[i]["vehicleBoxSetId"]
        print("vehicleBoxSetId:", self.g["vehicleBoxSetId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑油水箱")
    def test_editvehicleBoxSet(self):
        """
            油水箱设置：编辑油水箱
        """
        self.g["name"] = "编辑" + self.g["name"]
        response = self.vehicleBoxSet.edit_vehicleBoxSet(self.req_url, self.g["Cookie"], self.g["vehicleBoxSetId"],
                                                         self.g["name"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除油水箱")
    def test_deletevehicleBoxSet(self):
        """
            油水箱设置：删除油水箱
        """
        response = self.vehicleBoxSet.delete_vehicleBoxSet(self.req_url, self.g["Cookie"], self.g["vehicleBoxSetId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
