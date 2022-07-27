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
