# Importing function to calculate days_in_units from another file (daysFunctions.py)
import daysFunctions as DaysFunctions
# Importing function to get user's input days to calculate
import userInput as UserInput
# Importing function to get user's input days to calculate but with try & Except block for text and float inputs
import userInputWithTryExcept as UserInputWithTryExcept
import MagicConst as magic


# Using while loop with True condition and break, just for example of using while loop
while magic.Earth_is_Round:
    # Using a function from imported file
    DaysFunctions.days_in_units(21, "seconds")
    # This while shouldn't start because Earth_is_round
    while magic.Earth_is_flat:
        print("we all should just drop from round Earth to the Space. So Earth is flat!!!!!!!")
    break

# using input from function from imported file
DaysFunctions.days_in_units(UserInput.input_days(), "minutes")
# using input from function from imported file with try/except block of code
DaysFunctions.days_in_units(UserInputWithTryExcept.input_days(), "hours")
