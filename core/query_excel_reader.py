# coding: utf-8
"""
@author: wangn8
@file: query_excel_reader.py
@time: 2021/11/30 18:18
"""
import os
from utils.log import get_logger
from utils.excel_utils import ExcelUtils
from constant import config, slot_path

log = get_logger()


class ExcelCollection:
    CATEGORY = 0
    MODULE = 1
    FEATURE = 2
    QUERY = 3
    DOMAIN = 4
    INTENT = 5
    SLOT = 6
    PROPERTY = 7
    CAR_TYPE = 8


class QueryExcelReader:
    def __init__(self, folder):
        self.config = config
        self.folder = folder

    def _get_all_excel(self):
        """获取所有excel文件名称"""
        excel_list = []
        for root, folders, files in os.walk(self.folder):
            for file in files:
                excel_list.append(self.config + file)
        return excel_list

    def read_excel_content(self):
        """读取excel所有的sheet的内容"""
        log.info("读取excel文件:")
        excels = self._get_all_excel()
        for idx, excel in enumerate(excels):
            log.info("\t{0}.{1}".format(idx, excel))
        all_sheet_querys = []
        for excel in excels:
            excel_reader = ExcelUtils(excel)
            sheets = excel_reader.get_sheets()
            # 读取excel内容
            for sheet in sheets:
                try:
                    all_sheet_querys.extend(self._get_sheet_content(excel_reader, sheet))
                except Exception as e:
                    log.info("Error: {}".format(e))
                    raise e
        return all_sheet_querys

    def _get_sheet_content(self, excel_obj, sheet):
        """读取表格内容"""
        excel_obj.set_table(sheet)
        sheet_lines = []
        log.info("\t\t正在读<{0}>".format(sheet.name))
        for row in range(1, excel_obj.rows):
            # 1.读取category、module、feature
            category = excel_obj.get_cell(row, ExcelCollection.CATEGORY)
            module = excel_obj.get_cell(row, ExcelCollection.MODULE)
            feature = excel_obj.get_cell(row, ExcelCollection.FEATURE)
            # 2.读取query, 并解析
            querys = excel_obj.get_cell(row, ExcelCollection.QUERY)
            # 2.1 解析query
            query_sentence = parse(querys.split("\n"))
            # 3.读取domain
            domain = excel_obj.get_cell(row, ExcelCollection.DOMAIN)
            # 4.读取intent, 并解析
            intent = excel_obj.get_cell(row, ExcelCollection.INTENT)
            # 4.1 解析Intent
            intent_sentence = parse(intent.split("\n"))
            # 5.读取slot, 并解析
            slot = excel_obj.get_cell(row, ExcelCollection.SLOT)
            if slot.endswith(".txt"):
                # 5.1 如果slot是".txt"结尾，代表这里要读取txt
                slot_sentence = slot_path + slot
            else:
                # 5.2 否则读取表格内容
                slot_sentence = parse(slot.split("\n"))
            # 6.读取优先级, 并解析
            property = excel_obj.get_cell(row, ExcelCollection.PROPERTY)
            property_sentence = parse(property.split("\n"))
            # 7.读取车型, 并解析
            car_type = excel_obj.get_cell(row, ExcelCollection.CAR_TYPE)
            car_type_sentence = parse(car_type.split("\n"))

            sheet_lines.append([category, module, feature, query_sentence, domain, intent_sentence, slot_sentence, property_sentence, car_type_sentence])
        return sheet_lines


def parse(lines):
    """分割数据"""
    cont = []
    for line in lines:
        data = line.split("#")
        if len(data) > 1 and data[1]:
            cont.append(data[1])
    return cont


if __name__ == '__main__':
    from constant import config
    qer = QueryExcelReader(config)
    excel_content = qer.read_excel_content()
    for ex in excel_content:
        print(ex)
