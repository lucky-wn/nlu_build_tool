# coding: utf-8
"""
@author: wangn8
@file: log.py
@time: 2021/11/5 15:41
"""
import logging
import logging.handlers
import datetime
import os

from constant import log


class Log(object):
    __flag = None

    def __new__(cls, *args, **kwargs):
        if not cls.__flag:
            cls.__flag = super().__new__(cls)
        return cls.__flag

    def __init__(self, path="all.log"):
        if 'logger' not in self.__dict__:
            logger = logging.getLogger('myLogger')
            logger.setLevel(logging.DEBUG)
            # 根据时间滚动,when=midnight表示凌晨12点开始记录日志,interval表示间隔,backupCount表示备份数量
            rf_handler = logging.handlers.TimedRotatingFileHandler(log + os.sep + path)
            rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

            f_handler = logging.FileHandler(log + os.sep + 'error.log')
            f_handler.setLevel(logging.ERROR)
            f_handler.setFormatter(
                logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"))

            logger.addHandler(rf_handler)
            logger.addHandler(f_handler)

            self.logger = logger

    def return_logger(self):
        return self.logger


def get_logger():
    return Log().return_logger()


# def get_logger():
#     logger = logging.getLogger('myLogger')
#     logger.setLevel(logging.DEBUG)
#     # 根据时间滚动,when=midnight表示凌晨12点开始记录日志,interval表示间隔,backupCount表示备份数量
#     rf_handler = logging.handlers.TimedRotatingFileHandler(log + os.sep + 'all.log')
#     rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
#
#     f_handler = logging.FileHandler(log + os.sep + 'error.log')
#     f_handler.setLevel(logging.ERROR)
#     f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"))
#
#     logger.addHandler(rf_handler)
#     logger.addHandler(f_handler)
#     return logger


if __name__ == '__main__':
    logger = get_logger()
    logger.debug("test debug")
    logger.error("test error")
