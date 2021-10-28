# -*- coding: utf-8 -*-
# @Time    : 2021-10-27
# @Author  : kuwanjun
# @File    : test_tree.py

import time
import random
from TestCase.initEnv import *
import unittest
from ApiCommon.tree_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.tree = Tree_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().g["Cookie"]

        LOG.info('【树种管理】测试用例开始执行')

    def tearDown(self):
        LOG.info('【树种管理】测试用例执行完毕')

    @logger("添加树种")
    def test_addtree(self):
        """
            树种管理：添加树种
        """
        self.g["treeName"] = "python树种" + str(random.randint(100, 999))
        response = self.tree.add_tree(self.req_url, self.g["Cookie"], self.g["treeName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询树种")
    def test_findtree(self):
        """
            树种管理：查询树种
        """
        response = self.tree.find_tree(self.req_url, self.g["Cookie"])
        pythontree = response["body"]["rows"]
        for i in range(0, len(pythontree)):
            if pythontree[i]["treeName"] == self.g["treeName"]:
                self.g["treeId"] = pythontree[i]["treeId"]
        print("treeId:", self.g["treeId"])
        assert self.initEvn.test.assert_in_text(response["body"], "python")

    @logger("编辑树种")
    def test_edittree(self):
        """
            树种管理：编辑树种
        """
        self.g["treeName"] = "编辑" + self.g["treeName"]
        response = self.tree.edit_tree(self.req_url, self.g["Cookie"], self.g["treeId"],
                                       self.g["treeName"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除树种")
    def test_deletetree(self):
        """
            树种管理：删除树种
        """
        response = self.tree.delete_tree(self.req_url, self.g["Cookie"], self.g["treeId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

