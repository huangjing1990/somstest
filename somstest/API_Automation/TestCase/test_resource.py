# -*- coding: utf-8 -*-
# @Time    : 2021-6-18
# @Author  : huangjing
# @File    : test_resource.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.resource_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestResource(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.resource = Resource_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加资源")
    def test_addresource(self):
        """
            资源管理：添加资源
        """
        response = self.resource.add_resource(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询资源")
    def test_findresource(self):
        """
            资源管理：查询资源
        """
        response = self.resource.find_resource(self.req_url, self.g["Cookie"])
        pythonresource = response["body"]["rows"]
        for i in range(0, len(pythonresource)):
            if pythonresource[i]["operationResourceName"] == "python资源":
                self.g["operationResourceId"] = pythonresource[i]["operationResourceId"]
        print("operationResourceId:", self.g["operationResourceId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑资源")
    def test_editresource(self):
        """
            资源管理：编辑资源
        """
        response = self.resource.edit_resource(self.req_url, self.g["Cookie"], self.g["operationResourceId"])
        assert self.initEvn.test.assert_body(response["body"], 'resultCode', 1)

    @logger("删除资源")
    def test_deleteresource(self):
        """
            资源管理：删除资源
        """
        response = self.resource.delete_resource(self.req_url, self.g["Cookie"], self.g["operationResourceId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
