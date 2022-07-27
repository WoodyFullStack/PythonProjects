import daysFunctions as DaysFunction


# added an input with converting it to a list, to count days in hours by DaysFunction function from other file.
def list_of_days():
    days_count_input = input("input a count of days to convert them to hours, with spaces between them\n")
    days_count_input = list(days_count_input.split())
    wrong_inputs = []
    for x in days_count_input:
        # just trying to convert it to integer, to proper count it in hours
        try:
            x = int(x)
            # if it < 0 - just don't convert it
            if x >= 0:
                DaysFunction.days_in_units(x, "hours")
            else:
                wrong_inputs.append(x)
        except ValueError:
            # if it's not an integer - just don't convert it
            wrong_inputs.append(x)
    # print list with wrong inputs only if we have em.
    if wrong_inputs:
        print(f"{wrong_inputs} is incorrect values")
