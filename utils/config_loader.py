#coding:utf-8
import configparser
from constant import project


class ConfigLoader:
    def __init__(self, name="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(name, encoding="utf-8")

    def get_value(self, section, option):

        return self.config.get(section, option)

    def get_options(self, section):
        return self.config.options(section)


if __name__ == '__main__':
    conf = ConfigLoader()
    print(conf.get_options('sentence'))