# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : test_add.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.org_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestOrg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.org = Org_interface()
        # cls.user_token, cls.appid = initEvn().get_userToken()
        cls.g = globals()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("登录")
    def test_login(self):
        """
            用例描述：登录
        """
        response = self.login.login(self.req_url, lu="209487", pd="DB1A8BD798EEA81B0BE3DCA1D0E2C309")
        print(response["headers"])
        self.g["Cookie"] = {"JSESSIONID": response["headers"]["Set-Cookie"][11:43]}
        print(self.g["Cookie"])
        assert self.initEvn.test.assert_code(response['code'], 302)

    @logger("添加单位")
    def test_addorg(self):
        """
            用例描述：添加单位
        """
        response = self.org.add_org(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
