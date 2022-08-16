"""This module just save new data to spreadsheet
and compare it to return that items if their cost is lower """

import openpyxl
from datetime import datetime
row_of_first_item = 3
spreadsheet = 'items.xlsx'
num_col = 1
url_col = 2
description_col = 3



def save_prices_to_table(list_of_items):
    """Parse incoming dictionary with list of items {'URL to item':[item_description, item price in Rubles])"""
    wb = openpyxl.load_workbook(spreadsheet)
    sheet = wb.active

    max_col = sheet.max_column
    urls = list(list_of_items.keys())

    for url in range(len(urls)):
        sheet.cell(row_of_first_item + url, num_col).value = url + 1
        sheet.cell(row_of_first_item + url, url_col).value = urls[url]

    for item in range(len(list_of_items)):
        sheet.cell(row_of_first_item + item, description_col).value = list_of_items.get(urls[item])[0]
        sheet.cell(row_of_first_item + item, max_col + 1).value = list_of_items.get(urls[item])[1]
        sheet.cell(row_of_first_item - 1, max_col + 1).value = datetime.date(datetime.today())
        wb.save(spreadsheet)


def compare_prices_with_the_past():
    """Check that prices in new colon is lower than prices in previous colon"""
    wb = openpyxl.load_workbook(spreadsheet)
    sheet = wb.active
    diference = []
    max_col = sheet.max_column
    max_row = sheet.max_row

    for item in range(0, max_row-row_of_first_item+1):
        if sheet.cell(row_of_first_item+item, max_col).value < sheet.cell(row_of_first_item+item, max_col-1).value:
            diference.append(f'Price for {sheet.cell(row_of_first_item+item, description_col).value} now is lower. \n'
                             f'Previous Price {sheet.cell(row_of_first_item+item, max_col-1).value} \n'
                             f'New Price {sheet.cell(row_of_first_item+item, max_col).value} \n'
                             f'Link to the Store: {sheet.cell(row_of_first_item+item, url_col).value})')
    return diference

