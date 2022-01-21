# -*- coding: utf-8 -*-
# @Time    : 2021-3-30
# @Author  : huangjing
# @File    : test_role.py
# 在研发与技术推广中心下，创建python用户，授权武汉研发专用的角色，后删除

import time
import random
from datetime import timedelta
from TestCase.initEnv import *
import unittest
from ApiCommon.user_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.user = User_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【用户管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【用户管理】测试用例执行完毕')

    @logger("添加用户")
    def test_adduser(self):
        """
            用户管理：添加用户
        """
        self.g["employeeId"] = str(random.randint(700000, 800000))
        self.g["username"] = "python用户" + str(random.randint(100, 1000))
        response = self.user.add_user(self.req_url, self.g["Cookie"], employeeId=self.g["employeeId"])
        # 在研发与推广中心下添加用户，部门id=1215，若部门不存在则该模块用例会执行失败。
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询用户")
    def test_findUserByOrg(self):
        """
            用户管理：查询用户
        """
        response = self.user.findUserByPage(self.req_url, self.g["Cookie"], employeeId=self.g["employeeId"])
        self.g["userId"] = response["body"]["rows"][0]["userId"]
        print(self.g["userId"])
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑用户")
    def test_edituser(self):
        """
            用户管理：编辑用户
        """
        self.g["username"] = "编辑" + self.g["username"]
        response = self.user.edit_user(self.req_url, self.g["Cookie"], userId=self.g["userId"],
                                       employeeId=self.g["employeeId"], username=self.g["username"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查看用户")
    def test_findUserById(self):
        """
            用户管理：查看用户
        """
        response = self.user.find_userById(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["username"])

    @logger("用户授权角色")
    def test_userHasRole(self):
        """
            用户管理：用户授权角色
        """
        response = self.user.edit_userHasRole(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("解锁")
    def test_unLockUser(self):
        """
            用户管理：解锁
        """
        response = self.user.unLockUser(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("密码重置")
    def test_resetPassword(self):
        """
            用户管理：密码重置
        """
        response = self.user.resetPassword(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除用户")
    def test_deleteUser(self):
        """
            用户管理：删除用户
        """
        response = self.user.delete_user(self.req_url, self.g["Cookie"], self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("登录历史")
    def test_loginHistory(self):
        """
            用户管理：登录历史
        """
        time_start = time.strftime("%Y-%m-%d")

        response = self.user.login_history(self.req_url, self.g["Cookie"], time_start, time_start)
        assert self.initEvn.test.assert_in_text(response['body'], "黄静")
