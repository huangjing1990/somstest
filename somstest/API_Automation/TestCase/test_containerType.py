# -*- coding: utf-8 -*-
# @Time    : 2021-10-25
# @Author  : kuwanjun
# @File    : test_containerType.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.containerType_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestContainerType(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.containerType = ContainerType_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【容器类型管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【容器类型管理】测试用例执行完毕')

    @logger("添加容器类型")
    def test_addcontainerType(self):
        """
            容器类型管理：添加容器类型
        """
        self.g["name"] = "python容器类型" + str(random.randint(100, 999))
        self.g["volume"] = str(random.randint(120, 480))
        response = self.containerType.add_containerType(self.req_url, self.g["Cookie"], self.g["name"],
                                                        self.g["volume"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询容器类型")
    def test_findcontainerType(self):
        """
            容器类型管理：查询容器类型
        """
        response = self.containerType.find_containerType(self.req_url, self.g["Cookie"])
        pythoncontainerType = response["body"]["rows"]
        for i in range(0, len(pythoncontainerType)):
            if pythoncontainerType[i]["name"] == self.g["name"]:
                self.g["typeId"] = pythoncontainerType[i]["typeId"]
        print("typeId:", self.g["typeId"])
        assert self.initEvn.test.assert_in_text(response["body"], self.g["name"])

    @logger("编辑容器类型")
    def test_editcontainerType(self):
        """
            容器类型管理：编辑容器类型
        """
        self.g["name"] = "编辑" + self.g["name"]
        response = self.containerType.edit_containerType(self.req_url, self.g["Cookie"], self.g["typeId"],
                                                         self.g["volume"], self.g["name"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除容器类型")
    def test_deletecontainerType(self):
        """
            容器类型管理：删除容器类型
        """
        response = self.containerType.delete_containerType(self.req_url, self.g["Cookie"], self.g["typeId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
