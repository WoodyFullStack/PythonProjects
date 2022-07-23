def days_in_units(days,unitstype):
    if unitstype == "hours":
        return print(f"{days} days are {days * 24} {unitstype}")
    if unitstype == "minutes":
        return print(f"{days} days are {days * 24 * 60} {unitstype}")
    if unitstype == "seconds":
        return print(f"{days} days are {days * 24 * 60 * 60} {unitstype}")

days_in_units(20,"seconds")
