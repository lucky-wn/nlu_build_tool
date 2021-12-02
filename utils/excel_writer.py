# coding:utf-8
import json
import os
import time

import xlwt
from constant import result


class ExcleWriter:

    def __init__(self, name="NLU_QUERY"):
        self.book = xlwt.Workbook()
        self.book.add_sheet("Sheet1")
        self.name = name
        self.sheet = self.book.get_sheet("Sheet1")

    def save(self):
        self.book.save(
            result + os.path.sep + self.name + "_%s" % time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".xls")

    def write(self, row, col, value):
        self.sheet.write(row, col, value)

    def write_data(self, index, result_list):
        self.sheet.write(index, 0, result_list[0])
        self.sheet.write(index, 1, result_list[1])
        self.sheet.write(index, 2, result_list[2])
        self.sheet.write(index, 3, result_list[3])
        self.sheet.write(index, 4, result_list[4])
        self.sheet.write(index, 5, result_list[5])
        self.sheet.write(index, 6, result_list[6])
        self.sheet.write(index, 7, result_list[7])
        self.sheet.write(index, 8, result_list[8])
        self.sheet.write(index, 9, result_list[9])
        self.sheet.write(index, 10, result_list[10])
        self.sheet.write(index, 11, result_list[11])

    def write_label(self):
        self.sheet.write(0, 0, label="Category")
        self.sheet.write(0, 1, label="Module")
        self.sheet.write(0, 2, label="Feature")
        self.sheet.write(0, 3, label="Query")
        self.sheet.write(0, 4, label="Domain")
        self.sheet.write(0, 5, label="Intent")
        self.sheet.write(0, 6, label="Slot")
        self.sheet.write(0, 7, label="优先级")
        self.sheet.write(0, 8, label="E28")
        self.sheet.write(0, 9, label="D55")
        self.sheet.write(0, 10, label="D22")
        self.sheet.write(0, 11, label="E28")


if __name__ == '__main__':
    ew = ExcleWriter("output")
    ew.write(0, 0, "feautre")
    ew.save()
