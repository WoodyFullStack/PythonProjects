# defining a function to use in main.py
def days_in_units(days, units_type):
    # If we
    if days is False:
        return print("you wrote wrong count of days")
    try:
        if units_type == "hours":
            return print(f"{days} days are {days * 24} {units_type}")
        if units_type == "minutes":
            return print(f"{days} days are {days * 24 * 60} {units_type}")
        if units_type == "seconds":
            return print(f"{days} days are {days * 24 * 60 * 60} {units_type}")
    except ValueError:
        return print(f"{days} is a wrong count of days")
