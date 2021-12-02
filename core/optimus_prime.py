# coding: utf-8
"""
@author: wangn8
@file: optimus_prime.py
@time: 2021/12/1 14:48
"""
import json


def match_infomation(query, intent_dic, slot_dict, property_dict):
    intent = ""
    slot = {}
    property = ""

    # match intent
    intent = _match(query, intent, intent_dic)
    # match slot
    slot = _match(query, slot, slot_dict)
    property = _match(query, property, property_dict)
    return intent, str(slot), property


def _match(query, sth, sth_dict):
    """匹配"""
    for key in sth_dict.keys():
        if sth:
            break
        for word in key.split("|"):
            if word in query:
                sth = sth_dict[key]
                break
    return sth


def build_matcher(sentences):
    """生成映射字典"""
    # 普通模式
    match_dict = {}
    if isinstance(sentences, list):
        for sent in sentences:
            key, value = sent.split("=")
            match_dict[key] = value
        return match_dict
    else:
        # txt模式
        with open(sentences, "r", encoding="utf8") as file:
            lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            key, value = line.split("=")
            match_dict[key] = value
        return match_dict


def build_query(sentences):
    """排列组合所有说法"""
    sentence_model = []
    for sent in sentences:
        if sent.replace("*", "|").split("|") not in sentence_model:
            sentence_model.append(sent.replace("*", "|").split("|"))

    # 生成query
    sentence_numb = len(sentence_model)
    total = 1
    for sm in sentence_model:
        total *= len(sm)
    all_querys = [''] * total

    for sm in sentence_model:
        all_querys.sort()
        for i in range(total):
            all_querys[i] += sm[i % len(sm)]
    return all_querys