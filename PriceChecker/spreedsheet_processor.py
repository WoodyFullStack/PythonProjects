"""This module just save new data to spreedsheet
and compare it to return that items if their cost is lower """

import openpyxl

def save_prices_to_table(list_of_items):
    """Parse incoming dictionary with list of items {'URL to item':[item_description, item price in Rubles])"""
    print(1)
    openpyxl.load_workbook()


def compare_prices_with_the_past():
    """Check that prices in new colon is lower than prices in previous colon"""
    print(2)
