# coding:utf-8
import xlrd
import xlwt

from constant import case


class ExcelUtils:
    def __init__(self, excel):
        self.excel = excel
        self.obj = xlrd.open_workbook(self.excel)
        self.table = None

    def get_sheets(self):
        return self.obj.sheets()

    def set_table(self, sheet_obj):
        """设置sheet对象"""
        self.table = sheet_obj

    @property
    def rows(self):
        return self.table.nrows

    @property
    def cols(self):
        return self.table.ncols

    def get_cols(self, sheet_name):
        pass

    def get_cell(self, row, col):
        return self.table.cell_value(row, col)


if __name__ == '__main__':
    eu = ExcelUtils("小程序.xls", "Sheet1")
    print(eu.features())