# coding: utf-8
"""
@author: wangn8
@file: get_conf.py
@time: 2021/10/8 16:13
"""
from utils.config_loader import ConfigLoader


class QueryConfig:
    def __init__(self, config_file):
        self.conf = ConfigLoader(config_file)

    def get_sentence(self, section='sentence'):
        sentence_list = []
        options = self.conf.get_options(section)
        for op in options:
            sentence_list.append(self.conf.get_value(section, op))
        return sentence_list

    def get_feature(self, section='feature'):
        return self.conf.get_value(section, 'feature')

    def get_intent(self, section='intent'):
        return self.conf.get_value(section, 'intent')

    def get_domain(self, section='domain'):
        return self.conf.get_value(section, 'domain')

    def get_slot(self, section='slot'):
        return self.conf.get_value(section, 'slot')


if __name__ == '__main__':
    conf = QueryConfig()
    print(conf.get_sentence())
    print(conf.get_feature())
    print(conf.get_intent())
    print(conf.get_domain())
    print(conf.get_slot())