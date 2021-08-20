# -*- coding: utf-8 -*-
# @Time    : 2021-6-23
# @Author  : huangjing
# @File    : test_operationTask.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.operation_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestHumanTasks(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.task = OperationTask_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加人工作业任务")
    def test_addtask(self):
        """
            人工作业任务管理：添加人工作业任务
        """
        response = self.task.add_task(self.req_url, self.g["Cookie"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询人工作业任务")
    def test_findtask(self):
        """
            人工作业任务管理：查询人工作业任务
        """
        response = self.task.find_task(self.req_url, self.g["Cookie"])
        pythontask = response["body"]["rows"]
        for i in range(0, len(pythontask)):
            if pythontask[i]["operationTaskName"] == "python人工作业任务":
                self.g["operationTaskId"] = pythontask[i]["operationTaskId"]
        print("operationTaskId:", self.g["operationTaskId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑人工作业任务")
    def test_edittask(self):
        """
            人工作业任务管理：编辑人工作业任务
        """
        response = self.task.edit_task(self.req_url, self.g["Cookie"], self.g["operationTaskId"])
        assert self.initEvn.test.assert_body(response["body"], 'resultCode', 1)

    @logger("删除人工作业任务")
    def test_deletetaske(self):
        """
            人工作业任务管理：删除人工作业任务
        """
        response = self.task.delete_task(self.req_url, self.g["Cookie"], self.g["operationTaskId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
