# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : Config.py

from configparser import ConfigParser
from Common import Log
import os
import yaml


class Config:
    # titles:
    TITLE_DEBUG = "somstest"
    TITLE_RELEASE = "somsprev"
    DB_DEBUG = "DBInfo"

    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_APIKEY = "apikey"
    VALUE_DBHOST = "dbhost"
    VALUE_DBUSERNAME = "dbusername"
    VALUE_DBPASSWORD = "dbpassword"
    VALUE_DBPORT = "dbport"
    VALUE_DBDATABASE = "dbdatabase"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')
        self.html_report_path = Config.path_dir + '/Report/html'
        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.dbhost_debug = self.get_conf(Config.DB_DEBUG, Config.VALUE_DBHOST)
        self.dbuser_debug = self.get_conf(Config.DB_DEBUG, Config.VALUE_DBUSERNAME)
        self.dbpassword_debug = self.get_conf(Config.DB_DEBUG, Config.VALUE_DBPASSWORD)
        self.dbport_debug = self.get_conf(Config.DB_DEBUG, Config.VALUE_DBPORT)
        self.dbdatabase_debug = self.get_conf(Config.DB_DEBUG, Config.VALUE_DBDATABASE)

        self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
