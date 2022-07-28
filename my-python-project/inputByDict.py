import daysFunctions as DaysFunctions


def dict_of_days():
    days_in_dict = {"days": input("Please write a count of days: "),
                    "type": input("Please write a type to what convert: ").lower()}
    try:
        if int(days_in_dict["days"]) > 0:
            if days_in_dict.get("type") == "hours" or "minutes" or "seconds":
                DaysFunctions.days_in_units(int(days_in_dict["days"]), days_in_dict["type"])
    except ValueError:
        print("You entered something wrong")
