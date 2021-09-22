# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : Request.py

"""
封装request

"""
import requests
import Common.Consts
from Common.log_Common import *
from Common.Assert import Assertions
import json
import urllib3

s = requests.Session()
test = Assertions()
urllib3.disable_warnings()


class Request:

    @logger('get_request')
    def get_request(self, url, data=None, header=None):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)

        try:
            if data is None:
                LOG.info('请求地址：%s' % (url))
                LOG.info('请求入参：%s' % (data))
                response = requests.get(url=url, headers=header, verify=False)
                assert test.assert_code(response.status_code, 200)
            else:
                LOG.info('请求地址：%s' % (url))
                LOG.info('请求入参：%s' % (data))
                response = requests.get(url=url, params=data, headers=header, verify=False)
                assert test.assert_code(response.status_code, 200)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total
        response_dicts['history'] = response.history
        if (len(response.json()) < 100):
            LOG.info(url + ': 返回结果：%s' % (response.json()))
        return response_dicts

    @logger('post_request')
    def post_request(self, url, params, header, cookie=None):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:a
        """
        if not url.startswith('https://'):
            url = '%s%s' % ('https://', url)
            print(url)
        ContentType = header.get("Content-Type")
        # if (cookie is not None):
        #     s.headers.update(cookie)
        try:
            if params is None:
                response = requests.post(url, data=None, headers=header, verify=False)
            else:
                if (ContentType == "application/json"):
                    data_str = json.dumps(params)
                else:
                    data_str = params
                LOG.info('请求地址：%s' % (url))
                LOG.info('请求入参：%s' % (data_str))
                LOG.info('请求header：%s' % (header))
                response = requests.post(url, data=data_str, headers=header, cookies=cookie, verify=False,
                                         allow_redirects=False)
                assert test.assert_code(response.status_code, 200)
                LOG.info('response.status_code：%s' % (response.status_code))
                s.close()

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return e

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return e

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        response_dicts['headers'] = response.headers
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        try:
            response_dicts['body'] = response.json()
            if (len(response.text) < 500):
                LOG.info(url + ': 返回结果：%s' % (response.json()))
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
            LOG.info(url + ': 返回结果：%s' % (response_dicts['body']))
        return response_dicts

    @logger('post_request_multipart')
    def post_request_multipart(self, url, header, file):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            LOG.info('请求地址：%s' % (url))
            files = open(file, 'rb')
            files = {
                'excelFile': files
            }
            LOG.info('请求地址files：%s' % (files))
            response = requests.post(url, files=files, headers=header, verify=False)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data, header):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=header)
            else:
                response = requests.put(url=url, params=data, headers=header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        Common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts
