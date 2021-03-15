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
        # self.g["goodId"] = response['body']["data"]
        assert self.initEvn.test.assert_in_response_text(response['text'], "迅洁智慧环卫")

    @logger("添加单位")
    def test_addorg(self):
        """
            用例描述：添加单位
        """
        # response = self.product.addproduct(self.req_url, token=self.user_token, appId=self.appid,
        #                                    name=self.productName)
        # self.g["goodId"] = response['body']["data"]
        # assert self.initEvn.test.assert_body(response['body'], 'code', '000000')
