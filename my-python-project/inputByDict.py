import daysFunctions as DaysFunctions


def dict_of_days():
    days_in_dict = {"days": int(input("Please write a count of days: ")),
                    "type": input("Please write a type to what convert: ").lower()}
    if days_in_dict["days"] > 0:
        if days_in_dict.get("type") == "Hours" or "minutes" or "seconds":
            DaysFunctions.days_in_units(int(days_in_dict.get("days")), days_in_dict.get("type"))
    else:
        print("You entered something wrong")
