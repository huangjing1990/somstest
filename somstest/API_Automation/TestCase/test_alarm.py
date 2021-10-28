# -*- coding: utf-8 -*-
# @Time    : 2021-10-28
# @Author  : huangjing
# @File    : test_alarm.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.alarm_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestAlarm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.alarm = Alarm_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【车辆报警设置】测试用例开始执行')

    def tearDown(self):
        LOG.info('【车辆报警设置】测试用例执行完毕')

    @logger("设置报警限制")
    def test_editalarm(self):
        """
            车辆报警设置：设置报警限制
        """
        response = self.alarm.edit_alarm(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询车辆报警设置")
    def test_findalarm(self):
        """
            车辆报警设置：查询车辆报警设置
        """
        response = self.alarm.find_alarm(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_in_text(response['body'], "疲劳驾驶")

