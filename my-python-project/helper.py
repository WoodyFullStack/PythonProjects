# defining a function to use in main.py
def days_in_units(days, units_type):
    # If we
    try:
        days = int(days)
        if units_type == "hours":
            return print(f"{days} days are {days * 24} {units_type}")
        elif units_type == "minutes":
            return print(f"{days} days are {days * 24 * 60} {units_type}")
        elif units_type == "seconds":
            return print(f"{days} days are {days * 24 * 60 * 60} {units_type}")
        else:
            return print("unsupported units")
    except ValueError:
        return print(f"{days} is a wrong count of days")


def input_days():
    # \n - moves blinking cursor to the next line
    return input("Please enter amount of days\n")


def dict_of_days():
    days_in_dict = {"days": input("Please write a count of days: "),
                    "type": input("Please write a type to what convert: ").lower()}
    return days_in_units(days_in_dict["days"], days_in_dict["type"])


def list_of_days():
    days_count_input = input("input a count of days to convert them to hours, with spaces between them\n")
    wrong_inputs = []
    for x in set(days_count_input.split()):
        try:
            x = int(x)
            if x >= 0:
                days_in_units(x, "hours")
            else:
                wrong_inputs.append(x)
        except ValueError:

            wrong_inputs.append(x)
    if wrong_inputs:
        print(f"{wrong_inputs} is incorrect values")


def input_days():
    # \n - moves blinking cursor to the next line
    days = input("Please enter amount of days\n")
    try:
        if int(days) >= 0:
            return int(days)
        else:
            return False
    except ValueError:
        return False
