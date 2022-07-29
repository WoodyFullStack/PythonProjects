import helper
from helper import *
from MagicConst import *


# added multiple variants for inputs
print("1. Automatic input")
print("2. Input by user with if/else statements")
print("3. Input by user with try/except statements")
print("4. Input with a list of days counts")
print("5. Input in a dictionary style")
dispatch_method_of_convert_days = ""

while dispatch_method_of_convert_days.lower() != "exit":
    dispatch_method_of_convert_days = input("Choose input method: ")
    if dispatch_method_of_convert_days == "1":
        while Earth_is_Round:
            days_in_units(21, "seconds")
            while Earth_is_flat:
                print("we all should just drop from round Earth to the Space. So Earth is flat!!!!!!!")
            break
    elif dispatch_method_of_convert_days == "2":
        # using input function from imported file
        days_in_units(input_days(), "minutes")
    elif dispatch_method_of_convert_days == "3":
        # using input function from imported file with try/except block of code
        days_in_units(input_days_try_except(), "hours")
    elif dispatch_method_of_convert_days == "4":
        list_of_days()
    elif dispatch_method_of_convert_days == "5":
        dict_of_days()
    elif dispatch_method_of_convert_days.lower() == "exit":
        print("ok, exit now")
    else:
        print("You entered wrong value")
