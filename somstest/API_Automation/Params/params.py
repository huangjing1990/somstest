# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : params.py

"""
定义所有测试数据

"""
from Params.tools import *
from Common import Log
from Common.log_Common import *

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(interface):
    data = ReadData().parse()
    param = data[interface]
    return param


# 解析测试用例数据,并组装
def request_data(interface, name):
    LOG.info('解析yaml, Path:' + path_dir + '/Params/Param/' + interface)
    params = get_parameter(interface)
    params_data = params[name]
    data = params_data[0]['data']
    url = params_data[0]['url']
    header = params_data[0]['header']
    return url, data, header
