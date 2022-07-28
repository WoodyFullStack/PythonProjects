import daysFunctions
import daysFunctions as DaysFunctions


def dict_of_days():
    days_in_dict = {"days": input("Please write a count of days: "),
                    "type": input("Please write a type to what convert: ").lower()}
    return daysFunctions.days_in_units(days_in_dict["days"],days_in_dict["type"])
