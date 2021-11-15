# -*- coding: utf-8 -*-
# @Time    : 2021-11-15
# @Author  : huangjing
# @File    : test_service.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.service_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.service = Service_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【服务单位管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【服务单位管理】测试用例执行完毕')

    @logger("添加服务单位")
    def test_addService(self):
        """
            服务单位管理：添加服务单位
        """
        self.g["serviceName"] = "python服务单位" + str(random.randint(100, 999))
        response = self.service.add_service(self.req_url, self.g["Cookie"], name=self.g["serviceName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询服务单位")
    def test_findService(self):
        """
            服务单位管理：查询服务单位
        """
        response = self.service.find_service(self.req_url, self.g["Cookie"], searchValue=self.g["serviceName"])
        pythonservice = response["body"]
        for i in range(0, len(pythonservice)):
            if pythonservice[i]["name"] == self.g["serviceName"]:
                self.g["cateringUnitsId"] = pythonservice[i]["cateringUnitsId"]
        print("cateringUnitsId:", self.g["cateringUnitsId"])
        assert self.initEvn.test.assert_in_text(response["body"], self.g["serviceName"])

    @logger("编辑服务单位")
    def test_editService(self):
        """
            服务单位管理：编辑服务单位
        """
        self.g["serviceName"] = "编辑" + self.g["serviceName"]
        response = self.service.edit_service(self.req_url, self.g["Cookie"], cateringUnitsId=self.g["cateringUnitsId"],
                                             name=self.g["serviceName"])
        assert self.initEvn.test.assert_body(response["body"], 'resultCode', 1)

    @logger("删除服务单位")
    def test_deleteService(self):
        """
            服务单位管理：删除服务单位
        """
        response = self.service.delete_service(self.req_url, self.g["Cookie"],
                                               cateringUnitsId=self.g["cateringUnitsId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
