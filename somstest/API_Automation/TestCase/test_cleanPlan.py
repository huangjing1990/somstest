# -*- coding: utf-8 -*-
# @Time    : 2022-1-27
# @Author  : huangjing
# @File    : test_cleanPlan.py
# 苏丽芳213492登录系统，进行收运计划的增删改查。部门id=1557，项目id=1276，收运路线自主创建。人员：郭华，车辆：鄂ABH599
# 本模块用例每月最后一天执行会存在问题，计划是当月的，而明细是下个月的。

import time
import calendar
import random
from datetime import datetime
from dateutils import relativedelta
from TestCase.initEnv import *
import unittest
from ApiCommon.cleanPlan_interface import *
from ApiCommon.cleanRoute_interface import *
from ApiCommon.Login_interface import *
from Params.params import *


class TestCleanPlan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.initEvn = initEvn()
        cls.req_url = cls.initEvn.host
        cls.login = Login_interface()
        cls.CleanPlan = CleanPlan_interface()
        cls.cleanRoute = CleanRoute_interface()
        cls.g = globals()
        cls.g["Cookie"] = initEvn().get_user1Cookie()

        LOG.info('【收运计划】测试用例开始执行')

    def tearDown(self):
        LOG.info('【收运计划】测试用例执行完毕')

    @logger("添加收运计划")
    def test_addCleanPlan(self):
        """
            收运计划：添加收运计划
        """

        self.g["cleanRouteName"] = "python收运路线" + str(random.randint(100, 999))
        self.cleanRoute.add_cleanRoute(self.req_url, self.g["Cookie"],
                                       cleanRouteName=self.g["cleanRouteName"])

        response2 = self.cleanRoute.find_cleanRoute(self.req_url, self.g["Cookie"])
        pythonRoute = response2["body"]["rows"]
        for i in range(0, len(pythonRoute)):
            if pythonRoute[i]["routeName"] == self.g["cleanRouteName"]:
                self.g["cleanRouteId"] = pythonRoute[i]["routeId"]

        month = time.strftime("%Y-%m")
        response3 = self.CleanPlan.add_cleanPlan(self.req_url, self.g["Cookie"],
                                                 routeIds=self.g["cleanRouteId"], month=month)
        assert self.initEvn.test.assert_body(response3['body'], 'resultCode', 1)

    @logger("查询收运计划")
    def test_findCleanPlan(self):
        """
            收运计划：查询收运计划
        """
        monthStart = time.strftime("%Y-%m-01 00:00:00")
        end = time.strftime("%Y-%m-01 23:59:59")
        end2 = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") + relativedelta(months=+1)
        monthEnd = datetime.strftime(end2, "%Y-%m-%d %H:%M:%S")
        response = self.CleanPlan.find_cleanPlan(self.req_url, self.g["Cookie"], monthStart=monthStart,
                                                 monthEnd=monthEnd)
        pythonPlan = response["body"]["rows"]
        for i in range(0, len(pythonPlan)):
            if pythonPlan[i]["routeId"] == self.g["cleanRouteId"]:
                self.g["cleanPlanId"] = pythonPlan[i]["cleanPlanId"]
        assert self.initEvn.test.assert_in_text(response['body'], self.g["cleanRouteName"])

    @logger("编辑收运计划")
    def test_editCleanPlan(self):
        """
            收运计划：编辑收运计划
        """
        month = time.strftime("%Y-%m")
        response = self.CleanPlan.edit_cleanPlan(self.req_url, self.g["Cookie"], cleanPlanId=self.g["cleanPlanId"],
                                                 month=month)
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("新建计划明细")
    def test_addCleanPlanDetail(self):
        """
            收运计划：新建计划明细
        """

        date1 = time.strftime("%Y-%m-%d")
        date2 = datetime.strptime(date1, "%Y-%m-%d") + relativedelta(days=+1)
        date = datetime.strftime(date2, "%Y-%m-%d")
        response = self.CleanPlan.add_cleanPlanDetail(self.req_url, self.g["Cookie"], cleanPlanId=self.g["cleanPlanId"],
                                                      date=date)
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("顺延明细")
    def test_postponeCleanPlanDetail(self):
        """
            收运计划：顺延明细
        """
        date1 = time.strftime("%Y-%m-%d")
        date2 = datetime.strptime(date1, "%Y-%m-%d") + relativedelta(days=+1)
        date = datetime.strftime(date2, "%Y-%m-%d")
        day1 = datetime.today()
        day2 = calendar.monthrange(day1.year, day1.month)
        days = day2[1] - day1.day - 1
        response = self.CleanPlan.postponeCleanPlanDetail(self.req_url, self.g["Cookie"],
                                                          cleanPlanId=self.g["cleanPlanId"], date=date, driverDays=days,
                                                          vehicleDays=days)
        assert self.initEvn.test.assert_in_text(response['body'], "郭华")

    @logger("提交审核")
    def test_submitCleanPlan(self):
        """
            收运计划：提交审核
        """
        self.g["cleanPlanIds"] = str(self.g["cleanPlanId"]) + ","
        response = self.CleanPlan.submitCleanPlan(self.req_url, self.g["Cookie"],
                                                  cleanPlanIds=self.g["cleanPlanIds"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    @logger("查询审核记录")
    def test_findCleanAuditing(self):
        """
            收运计划：查询审核记录
        """
        monthStart = time.strftime("%Y-%m-01 00:00:00")
        end = time.strftime("%Y-%m-01 23:59:59")
        end2 = datetime.strptime(end, "%Y-%m-%d %H:%M:%S") + relativedelta(months=+1)
        monthEnd = datetime.strftime(end2, "%Y-%m-%d %H:%M:%S")
        response = self.CleanPlan.findCleanAuditing(self.req_url, self.g["Cookie"], monthStart=monthStart,
                                                 monthEnd=monthEnd)
        assert self.initEvn.test.assert_in_text(response['body'], str(self.g["cleanPlanId"]))

    @logger("审核通过")
    def test_cleanAuditing(self):
        """
            收运计划：审核通过
        """
        response = self.CleanPlan.cleanAuditing(self.req_url, self.g["Cookie"],
                                                  cleanPlanIds=self.g["cleanPlanId"])
        assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)

    # @logger("删除收运计划")
    # def test_deleteCleanPlan(self):
    #     """
    #         收运计划：删除收运计划
    #     """
    #     response = self.CleanPlan.delete_cleanPlan(self.req_url, self.g["Cookie"], self.g["CleanPlanId"])
    #     assert self.initEvn.test.assert_body(response['body'], 'resultCode', 1)
