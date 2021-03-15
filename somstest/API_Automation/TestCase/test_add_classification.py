# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : test_add.py

import time
from TestCase.initEnv import *
import unittest
from ApiCommon.product_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestAddClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.product = Product_interface()
        cls.login = Login_interface()
        cls.user_token, cls.appid = initEvn().get_userToken()
        # 商品名称
        cls.productName = "测试" + str(int(time.time()))
        cls.goodsName = "测试" + str(int(time.time()))

        cls.g = globals()

        LOG.info('测试用例开始执行')

    def tearDown(self):
        LOG.info('测试用例执行完毕')

    @logger("添加商品信息")
    def test_addproduct(self):
        """
            用例描述：添加商品信息
        """
        response = self.product.addproduct(self.req_url, token=self.user_token, appId=self.appid,
                                           name=self.productName)
        self.g["goodId"] = response['body']["data"]
        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("新增商品分类")
    def test_addclassification(self):
        """
            用例描述：新增商品分类
        """
        response = self.product.add_classification(self.req_url, token=self.user_token, appId=self.appid,
                                                   name=self.productName)

        self.g["classId"] = response['body']["data"]
        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("确认商品分类添加成功")
    def test_getInfos(self):
        """
            用例描述：确认商品分类添加成功
        """
        response = self.product.getInfos(self.req_url, token=self.user_token, appId=self.appid)

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("搜索要更新的商品")
    def test_getDetails(self):
        """
            用例描述：搜索要更新的商品
        """
        response = self.product.getDetails(self.req_url, token=self.user_token, appId=self.appid,
                                           keyword=self.goodsName)

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("切换商品到新的分类")
    def test_updateRelationships(self):
        """
            用例描述：切换商品到新的分类
        """
        response = self.product.updateRelationships(self.req_url, token=self.user_token, appId=self.appid,
                                                    classificationIds=[self.g["classId"]], goodsIds=[self.g["goodId"]])

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("确认商品到新的分类成功")
    def test_isgetDetails(self):
        """
            用例描述：确认商品到新的分类成功
        """
        response = self.product.isgetDetails(self.req_url, token=self.user_token, appId=self.appid,
                                             classificationId=self.g["classId"])

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("下架商品")
    def test_apply(self):
        """
            用例描述：下架商品
        """
        response = self.product.apply(self.req_url, token=self.user_token, appId=self.appid,
                                      ids=[self.g["goodId"]])

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("移除商品")
    def test_remove(self):
        """
            用例描述：移除商品
        """
        response = self.product.remove(self.req_url, token=self.user_token, appId=self.appid,
                                       ids=[self.g["goodId"]])

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("删除分类信息")
    def test_deleteClass(self):
        """
            用例描述：删除分类信息
        """
        response = self.product.deleteClass(self.req_url, token=self.user_token, appId=self.appid,
                                            id=self.g["classId"])

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')

    @logger("退出登录")
    def test_logout(self):
        """
            用例描述：退出登录
        """
        response = self.login.logout(self.req_url, token=self.user_token, appId=self.appid)

        assert self.initEvn.test.assert_body(response['body'], 'code', '000000')
