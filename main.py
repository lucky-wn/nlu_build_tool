# coding: utf-8
"""
@author: wangn8
@file: main.py
@time: 2021/12/1 14:23
"""
import os

from core.optimus_prime import build_query, build_matcher, match_infomation
from core.query_excel_reader import QueryExcelReader
from constant import config, log
from utils.log import get_logger
from utils.excel_writer import ExcleWriter

logger = get_logger()

QUERY = 3
INTENT = 5
SLOT = 6
PROPERTY = 7
CAR_TYPE = 8

with open(log + "all.log", "w", encoding="utf8"):
    pass

logger.info("NLU Create Script Start...")
input_contents = QueryExcelReader(config).read_excel_content()
excel_writer = ExcleWriter()
excel_writer.write_label()
logger.info("Build Query Information...")
index = 1
for conts in input_contents:
    # 1.生成query
    querys = build_query(conts[QUERY])
    # 2.intent matcher
    intent_dict = build_matcher(conts[INTENT])
    # 3.slot matcher
    slot_dict = build_matcher(conts[SLOT])
    # 4.property matcher
    property_dict = build_matcher(conts[PROPERTY])
    # 5.car type =
    # 5.遍历生成的query，匹配数据，写入excel
    for query in querys:
        intent, slot, property = match_infomation(query, intent_dict, slot_dict, property_dict)
        if query:
            excel_writer.write_data(index, [conts[0],
                                            conts[1],
                                            conts[2],
                                            query,
                                            conts[4],
                                            intent,
                                            slot,
                                            property if property else "P0",
                                            "√" if "E28" in conts[CAR_TYPE] else "x",
                                            "√" if "D55" in conts[CAR_TYPE] else "x",
                                            "√" if "D22" in conts[CAR_TYPE] else "x",
                                            "√" if "E38" in conts[CAR_TYPE] else "x"])
            index += 1
excel_writer.save()
logger.info("NLU Create Script END...")
