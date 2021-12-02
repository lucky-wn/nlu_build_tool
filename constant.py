# coding: utf-8
"""
@author: wangn8
@file: constant.py
@time: 2021/9/22 21:01
"""
import os

project = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
result = project + "Result" + os.path.sep
data = project + os.path.sep + "data" + os.path.sep
case = project + "case" + os.path.sep
process = project + "process" + os.path.sep
nlu_result = project + "nlu_result" + os.path.sep
na = project + "na" + os.path.sep
config = project + "config" + os.path.sep
log = project + "logs" + os.path.sep
slot_path = project + "slot" + os.path.sep
print(project)