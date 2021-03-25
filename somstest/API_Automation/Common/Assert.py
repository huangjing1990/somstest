# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : Assert.py


"""
封装Assert方法

"""
from Common import Log
from Common.log_Common import *
from Common import Consts
import json
import re


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    @logger('状态码断言')
    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            if (code == 302):  # 如果状态码是302，说明请求正常
                LOG.info(" statusCode is %s " % (code))
                return True
            assert code == expected_code
            LOG.info(" statusCode is %s " % (code))
            return True
        except:
            LOG.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            raise

    @logger('验证response body中任意属性的值')
    def assert_body(self, body, body_msg, expected_msg, msgs=None):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        msg = body[body_msg]
        try:
            assert msg == expected_msg
            LOG.info(" body_msg is %s " % (msg))
            return True

        except:
            LOG.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s,module is %s" % (
                expected_msg, msg, msgs))
            raise

    @logger('验证response body中是否包含预期字符串')
    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            LOG.info(" body_msg is %s " % (text))
            assert expected_msg in text
            return True

        except:
            LOG.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            raise

    @logger('验证response body中是否等于预期字符串')
    def assert_text(self, body, expected_msg, msg=None):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            LOG.info(" body_msg is %s " % (body))
            return True

        except:

            LOG.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s,module is %s" % (
                expected_msg, body, msg))

            raise

    @logger(' 验证response body响应时间小于预期最大响应时间,单位：毫秒')
    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            LOG.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            raise

    @logger(' 验证response body result 结果是否为空')
    def assert_length(self, length, expected_length, msg):
        """
        验证response body result 结果是否为空
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert len(length) == expected_length
            return True

        except:
            LOG.error("Response length > expected_length, expected_length is %s, Response length is %s，msg is %s" % (
                expected_length, len(length), msg))
            raise

    @logger('验证response text中是否包含预期字符串')
    def assert_in_response_text(self, text, expected_msg):
        """
        验证response text中是否包含预期字符串
        :param text:
        :param expected_msg:
        :return:
        """
        try:
            # text = json.dumps(responseText, ensure_ascii=False)
            LOG.info(" text_msg is %s " % (expected_msg))
            assert expected_msg in text
            return True

        except:
            LOG.error("Response text Does not contain expected_msg, expected_msg is %s" % expected_msg)
            raise
