# Importing function to calculate days_in_units from another file (daysFunctions.py)
import daysFunctions as DaysFunctions
# Importing function to get user's input days to calculate
import userInput as UserInput

# Using a function from imported file
DaysFunctions.days_in_units(21, "seconds")

# using input and convert it to int to calculate
DaysFunctions.days_in_units(int(UserInput.input_days()), "minutes")
