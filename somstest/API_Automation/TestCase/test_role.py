# -*- coding: utf-8 -*-
# @Time    : 2021-3-26
# @Author  : huangjing
# @File    : test_role.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.role_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestRole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.role = Role_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【角色管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【角色管理】测试用例执行完毕')

    @logger("添加角色")
    def test_addrole(self):
        """
            角色管理：添加角色
        """
        response = self.role.add_role(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询角色")
    def test_findrole(self):
        """
            角色管理：查询角色
        """
        response = self.role.find_role(self.req_url, self.g["Cookie"])
        pythonrole = response["body"]["rows"]
        for i in range(0, len(pythonrole)):
            if pythonrole[i]["roleName"] == "python角色":
                self.g["roleId"] = pythonrole[i]["roleId"]
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑角色")
    def test_editrole(self):
        """
            角色管理：编辑角色
        """
        response = self.role.edit_role(self.req_url, self.g["Cookie"], self.g["roleId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除角色")
    def test_deleterole(self):
        """
            角色管理：删除角色
        """
        response = self.role.delete_role(self.req_url, self.g["Cookie"], self.g["roleId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
