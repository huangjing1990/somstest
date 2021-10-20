# -*- coding: utf-8 -*-
# @Time    : 2021-9-26
# @Author  : huangjing
# @File    : test_mechanicalTask.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.mechanicalTask_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestMechanicalTasks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.tasks = MechanicalTask_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【机械任务】测试用例开始执行')

    def tearDown(self):
        LOG.info('【机械任务】测试用例执行完毕')

    @logger("添加机械任务")
    def test_addtask(self):
        """
            机械任务：添加机械任务
        """
        response = self.tasks.add_task(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询机械任务")
    def test_findtask(self):
        """
            机械任务：查询机械任务
        """
        response = self.tasks.find_task(self.req_url, self.g["Cookie"])
        pythontask = response["body"]["rows"]
        for i in range(0, len(pythontask)):
            if pythontask[i]["jobTypeName"] == "python机械作业任务":
                self.g["jobTypeId"] = pythontask[i]["jobTypeId"]
        print("jobTypeId:", self.g["jobTypeId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑机械任务")
    def test_edittask(self):
        """
            机械任务：编辑机械任务
        """
        response = self.tasks.edit_task(self.req_url, self.g["Cookie"], self.g["jobTypeId"])
        assert self.initEvn.test.assert_body(response["body"], 'resultCode', 1)

    @logger("删除机械任务")
    def test_deletetask(self):
        """
            机械任务：删除机械任务
        """
        response = self.tasks.delete_task(self.req_url, self.g["Cookie"], self.g["jobTypeId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
