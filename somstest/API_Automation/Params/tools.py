# -*- coding: utf-8 -*-
# @Time    : 2021-3-5
# @Author  : huangjing
# @File    : tools.py

"""
读取yaml测试数据

"""

import yaml
import os
import os.path


class ReadData():

    def parse(self):
        path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/Param'
        pages = {}
        for root, dirs, files in os.walk(path_ya):
            for name in files:
                watch_file_path = os.path.join(root, name)
                with open(watch_file_path, 'r', encoding='UTF-8') as f:
                    page = yaml.safe_load(f)
                    pages.update(page)
            return pages
