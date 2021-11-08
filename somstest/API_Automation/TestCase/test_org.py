# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : test_org.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.org_interface import *
from ApiCommon.Login_interface import *
from Params.params import *
import json


class TestOrg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.org = Org_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_adminCookie()

        LOG.info('【单位管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【单位管理】测试用例执行完毕')

    # @logger("登录")
    # def test_login(self):
    #     """
    #         用例描述：登录
    #     """
    #     response = self.login.login(self.req_url, lu="209487", pd="DB1A8BD798EEA81B0BE3DCA1D0E2C309")
    #     print(response["headers"])
    #     self.g["Cookie"] = {"JSESSIONID": response["headers"]["Set-Cookie"][11:43]}
    #     print(self.g["Cookie"])
    #     assert self.initEvn.test.assert_code(response['code'], 302)

    @logger("添加单位")
    def test_addorg(self):
        """
            单位管理：添加单位
        """
        response = self.org.add_org(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询单位")
    def test_findorg(self):
        """
            单位管理：查询单位
        """
        response = self.org.find_org(self.req_url, self.g["Cookie"])
        pythonorg = response["body"]["rows"][0]["children"][22]["children"][8]["children"]
        # 新安洁股份-新安洁重庆公司-两江新区项目公司-python部门，注意此处如果单位管理结构上变动了，索引也会跟着变动。
        for i in range(0, len(pythonorg)):
            if pythonorg[i]["orgName"] == "python部门":
                self.g["orgId"] = pythonorg[i]["orgId"]
        print(self.g["orgId"])
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑单位")
    def test_editorg(self):
        """
            单位管理：编辑单位
        """
        self.g["orgName"] = "编辑python部门"
        response = self.org.edit_org(self.req_url, self.g["Cookie"], self.g["orgId"], self.g["orgName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除单位")
    def test_deleteorg(self):
        """
            单位管理：删除单位
        """
        response = self.org.delete_org(self.req_url, self.g["Cookie"], self.g["orgId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("添加班组")
    def test_addteam(self):
        """
            班组管理：添加班组
        """
        response = self.org.add_team(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询班组")
    def test_findteam(self):
        """
            班组管理：查询班组
        """
        response = self.org.find_team(self.req_url, self.g["Cookie"])
        self.g["teamId"] = response["body"]["rows"][0]["orgId"]
        # print(self.g["teamId"])
        assert self.initEvn.test.assert_in_text(response['body'], "python")

    @logger("编辑班组")
    def test_editteam(self):
        """
            班组管理：编辑班组
        """
        response = self.org.edit_team(self.req_url, self.g["Cookie"], self.g["teamId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除班组")
    def test_deleteteam(self):
        """
            班组管理：删除班组
        """
        response = self.org.delete_team(self.req_url, self.g["Cookie"], self.g["teamId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
