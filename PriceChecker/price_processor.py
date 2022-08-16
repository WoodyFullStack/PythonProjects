import price_getter
import spreadsheet_processor

def check_prices():
    list_of_items = price_getter.get_desc_and_prices()
    spreadsheet_processor.save_prices_to_table(list_of_items)
    return spreadsheet_processor.compare_prices_with_the_past()

