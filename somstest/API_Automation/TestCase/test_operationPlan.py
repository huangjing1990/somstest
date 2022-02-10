# -*- coding: utf-8 -*-
# @Time    : 2022-2-8
# @Author  : luojun
# @File    : test_operationPlan.py
# 肖海波009269登录系统，进行人工计划的增删改查。部门id=1053（大竹林项目部），项目ID=5，青竹东路下自动创建路段。班组id：1061渝美班组，自动创建人员
# 本模块用例每月最后一天执行会存在问题，计划是当月的，而明细是下个月的。

import time
import calendar
import random
from datetime import datetime
from dateutils import relativedelta
from TestCase.initEnv import *
import unittest
from ApiCommon.operationPlan_interface import *
from ApiCommon.roadSection_interface import *
from ApiCommon.Login_interface import *
from ApiCommon.user_interface import *
from Params.params import *


class TestOperationPlan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.OperationPlan = OperationPlan_interface()
        cls.RoadSection = RoadSection_interface()
        cls.user = User_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_userCookie()

        LOG.info('【人工计划】测试用例开始执行')

    def tearDown(self):
        LOG.info('【人工计划】测试用例执行完毕')

    @logger("添加人工计划")
    def test_addOperationPlan(self):
        """
            人工计划：添加人工计划
        """

        self.g["roadSectionName"] = "python路段" + str(random.randint(100, 999))
        self.RoadSection.add_roadSection(self.req_url, self.g["Cookie"],
                                         roadSectionName=self.g["roadSectionName"])

        response2 = self.RoadSection.find_roadSection(self.req_url, self.g["Cookie"])
        pythonRoad = response2["body"]["rows"]
        for i in range(0, len(pythonRoad)):
            if pythonRoad[i]["roadSectionName"] == self.g["roadSectionName"]:
                self.g["roadSectionIds"] = pythonRoad[i]["roadSectionId"]

        month = time.strftime("%Y-%m")
        response3 = self.OperationPlan.add_operationPlan(self.req_url, self.g["Cookie"],
                                                         roadSectionIds=self.g["roadSectionIds"], month=month)
        assert self.initEvn.test.assert_body(response3['body'], 'resultCode', 1)

    @logger("查询人工计划")
    def test_findOperationPlan(self):
        """
            人工计划：查询人工计划
        """
        monthStart = time.strftime("%Y-%m-01 00:00:00")
        end = time.strftime("%Y-%m-01 23:59:59")
        end2 = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") + relativedelta(months=+1)
        monthEnd = datetime.strftime(end2, "%Y-%m-%d %H:%M:%S")
        response = self.OperationPlan.find_operationPlan(self.req_url, self.g["Cookie"], monthStart=monthStart,
                                                         monthEnd=monthEnd, roadSectionIds=self.g["roadSectionIds"])
        pythonPlan = response["body"]["rows"]
        for i in range(0, len(pythonPlan)):
            if pythonPlan[i]["roadSectionId"] == self.g["roadSectionIds"]:
                self.g["operationPlanId"] = pythonPlan[i]["operationPlanId"]
                print(self.g["operationPlanId"])
        assert self.initEvn.test.assert_in_text(response['body'], self.g["roadSectionName"])

    @logger("编辑人工计划")
    def test_editOperationPlan(self):
        """
            人工计划：编辑人工计划
        """
        month = time.strftime("%Y-%m")
        response = self.OperationPlan.edit_operationPlan(self.req_url, self.g["Cookie"],
                                                         operationPlanId=self.g["operationPlanId"],
                                                         month=month)
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("新建计划明细")
    def test_addOperationPlanDetail(self):
        """
            人工计划：新建计划明细
        """

        date1 = time.strftime("%Y-%m-%d")
        date2 = datetime.strptime(date1, "%Y-%m-%d") + relativedelta(days=+1)
        date = datetime.strftime(date2, "%Y-%m-%d")

        self.g["employeeId"] = str(random.randint(700000, 800000))
        self.g["username"] = "python用户" + str(random.randint(100, 1000))
        response1 = self.user.add_user(self.req_url, self.g["Cookie"], employeeId=self.g["employeeId"], orgId="1061",
                                       username=self.g["username"])
        # 查询用户
        response2 = self.user.findUserByPage(self.req_url, self.g["Cookie"], employeeId=self.g["employeeId"],
                                             orgdetpIds="[1061]")
        self.g["userId"] = response2["body"]["rows"][0]["userId"]
        print(self.g["userId"])

        response = self.OperationPlan.add_PlanDetail(self.req_url, self.g["Cookie"],
                                                     operationPlanId=self.g["operationPlanId"], date=date,
                                                     usersId=self.g["userId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("顺延计划明细")
    def test_postponeOperationPlanDetail(self):
        """
            人工计划：顺延明细
        """
        date1 = time.strftime("%Y-%m-%d")
        date2 = datetime.strptime(date1, "%Y-%m-%d") + relativedelta(days=+1)
        date = datetime.strftime(date2, "%Y-%m-%d")
        day1 = datetime.today()
        day2 = calendar.monthrange(day1.year, day1.month)
        days = day2[1] - day1.day - 1
        response = self.OperationPlan.postponePlanDetail(self.req_url, self.g["Cookie"],
                                                         operationPlanId=self.g["operationPlanId"],
                                                         roadSectionId=self.g["roadSectionIds"], date=date,
                                                         taskdays=days,
                                                         userdays=days)
        assert self.initEvn.test.assert_in_text(response['body'], self.g["username"])

    @logger("提交审核")
    def test_submitCleanPlan(self):
        """
            人工计划：提交审核
        """
        self.g["operationPlanIds"] = str(self.g["operationPlanId"]) + ","
        response = self.OperationPlan.submitOperationPlan(self.req_url, self.g["Cookie"],
                                                          operationPlanIds=self.g["operationPlanIds"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询审核记录")
    def test_findCleanAuditing(self):
        """
            人工计划：查询审核记录
        """
        monthStart = time.strftime("%Y-%m-01 00:00:00")
        end = time.strftime("%Y-%m-01 23:59:59")
        end2 = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") + relativedelta(months=+1)
        monthEnd = datetime.strftime(end2, "%Y-%m-%d %H:%M:%S")
        response = self.OperationPlan.findOperationAuditing(self.req_url, self.g["Cookie"], monthStart=monthStart,
                                                            monthEnd=monthEnd)
        assert self.initEvn.test.assert_in_text(response['body'], str(self.g["operationPlanId"]))

    @logger("审核通过")
    def test_createAuditing(self):
        """
            人工计划：审核通过
        """
        response = self.OperationPlan.createAuditing(self.req_url, self.g["Cookie"],
                                                     operationPlanIds=self.g["operationPlanId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("下发计划")
    def test_issueOperationPlan(self):
        """
            人工计划：下发计划
        """
        response = self.OperationPlan.issueOperationPlan(self.req_url, self.g["Cookie"],
                                                         operationPlanIds=self.g["operationPlanId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("顺延计划")
    def test_postponePlan(self):
        """
            人工计划：顺延计划
        """
        response = self.OperationPlan.postponePlan(self.req_url, self.g["Cookie"],
                                                   operationPlanIds=self.g["operationPlanId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("删除人工计划")
    def test_deleteOperationPlan(self):
        """
            人工计划：删除人工计划
        """
        response = self.OperationPlan.deleteOperationPlan(self.req_url, self.g["Cookie"],
                                                          operationPlanId=self.g["operationPlanId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 2)
