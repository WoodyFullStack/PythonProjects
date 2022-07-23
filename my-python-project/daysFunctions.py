def days_in_units(days, units_type):
    if units_type == "hours":
        return print(f"{days} days are {days * 24} {units_type}")
    if units_type == "minutes":
        return print(f"{days} days are {days * 24 * 60} {units_type}")
    if units_type == "seconds":
        return print(f"{days} days are {days * 24 * 60 * 60} {units_type}")
