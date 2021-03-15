# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : initEnv.py

from Conf.Config import Config
from ApiCommon.Login_interface import *
from Common import Request
from Common import Assert
from Params.params import *


class initEvn():

    def __init__(self):
        conf = Config()
        self.request = Request.Request()
        self.host = conf.host_debug
        self.test = Assert.Assertions()
        self.login = Login_interface()
        self.g = globals()

        # 定义报告详情

    def test_report(self):
        conf = Config()
        env = "private_debug"
        conf.set_conf(env, "versioncode", "V3.5")
        tester = conf.get_conf(env, "tester")
        environment = conf.get_conf(env, "environment")
        versioncode = conf.get_conf(env, "versioncode")

        details = tester + "_" + environment + versioncode
        return details

    def get_userToken(self):
        # 用户登录

        token, appid = self.login.login(self.host, phoneNumber="15527060286", password="hbc23687")

        # 获取 用户token

        user_token = self.login.get_userToken(self.host, appId=appid, token=token)

        return user_token, appid


if __name__ == '__main__':
    print(initEvn().get_userToken())
