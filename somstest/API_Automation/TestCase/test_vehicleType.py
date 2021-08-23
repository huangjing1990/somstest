# -*- coding: utf-8 -*-
# @Time    : 2021-8-23
# @Author  : huangjing
# @File    : test_vehicleType.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.vehicleType_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestVehicleType(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.vehicleType = VehicleType_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加车辆类型")
    def test_addVehicleType(self):
        """
            车辆类型管理：添加车辆类型
        """
        response = self.vehicleType.add_vehicleType(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询车辆类型")
    def test_findVehicleType(self):
        """
            车辆类型管理：查询车辆类型
        """
        response = self.vehicleType.find_vehicleType(self.req_url, self.g["Cookie"])
        pythonrole = response["body"]["rows"]
        for i in range(0, len(pythonrole)):
            if pythonrole[i]["workTypeName"] == "python车辆类型":
                self.g["workTypeId"] = pythonrole[i]["workTypeId"]
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑车辆类型")
    def test_editVehicleType(self):
        """
            车辆类型管理：编辑车辆类型
        """
        response = self.vehicleType.edit_vehicleType(self.req_url, self.g["Cookie"], self.g["workTypeId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除车辆类型")
    def test_deleteVehicleType(self):
        """
            车辆类型管理：删除车辆类型
        """
        response = self.vehicleType.delete_vehicleType(self.req_url, self.g["Cookie"], self.g["workTypeId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
