# -*- coding: utf-8 -*-
# @Time    : 2022-2-9
# @Author  : huangjing
# @File    : test_vehicleDriving.py
# 实时定位和轨迹回放，使用209487登录，查看车辆（渝BY2003）(id=10015)实时定位，从实时定位页面跳转至轨迹回放。
# 注意：车辆取的是2022-2-7日的数据，测试数据库只同步近两个月的数据，可能导致查不出轨迹回放。

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.vehicleDriving_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestVehicleDriving(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.vehicleDriving = VehicleDriving_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【实时定位】测试用例开始执行')

    def tearDown(self):
        LOG.info('【实时定位】测试用例执行完毕')

    @logger("查询实时定位")
    def test_getVehicleLatestPosition(self):
        """
            实时定位：查询车辆实时定位
        """
        response = self.vehicleDriving.getVehicleLatestPosition(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], "渝BY2003")

    @logger("查询车辆信息框")
    def test_getVehiclestate(self):
        """
            实时定位：查询车辆信息框
        """
        response = self.vehicleDriving.getVehiclestate(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], "渝BY2003")

    @logger("轨迹回放")
    def test_getTrajectory(self):
        """
            实时定位：轨迹回放
        """
        response = self.vehicleDriving.getTrajectory(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], "渝BY2003")
