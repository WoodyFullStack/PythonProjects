import file_processor
import price_getter
import spreadsheet_processor


def bot_check_price(user_id):
    list_of_items = price_getter.dns_get_desc_and_prices(user_id)
    spreadsheet_processor.save_prices_to_table(list_of_items, user_id)
    return spreadsheet_processor.compare_prices_with_the_past(user_id)


def bot_get_list(user_id):
    return price_getter.get_list_of_items(user_id)


def bot_check_user(user_id):
    return file_processor.check_user(user_id)


def bot_register(user_id):
    if file_processor.check_user(user_id) == "doesn't exists":
        file_processor.create_user_files(user_id)

print(bot_get_list(748906752))