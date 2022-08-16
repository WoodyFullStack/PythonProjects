"""This module just save new data to spreadsheet
and compare it to return that items if their cost is lower """

import openpyxl
from datetime import datetime
row_of_first_item = 3


def save_prices_to_table(list_of_items):
    """Parse incoming dictionary with list of items {'URL to item':[item_description, item price in Rubles])"""
    wb = openpyxl.load_workbook('items.xlsx')
    sheet = wb.active

    max_col = sheet.max_column
    urls = list(list_of_items.keys())

    for url in range(len(urls)):
        sheet.cell(row_of_first_item + url, 1).value = url + 1
        sheet.cell(row_of_first_item + url, 2).value = urls[url]

    for item in range(len(list_of_items)):
        sheet.cell(row_of_first_item + item, 3).value = list_of_items.get(urls[item])[0]
        sheet.cell(row_of_first_item + item, max_col + 1).value = list_of_items.get(urls[item])[1]
        sheet.cell(row_of_first_item - 1, max_col + 1).value = datetime.date(datetime.today())
        wb.save('items.xlsx')


def compare_prices_with_the_past():
    """Check that prices in new colon is lower than prices in previous colon"""
    print(2)