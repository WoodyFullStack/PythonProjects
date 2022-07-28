# Importing function to calculate days_in_units from another file (daysFunctions.py)
import daysFunctions as DaysFunctions
# Importing function to get user's input days to calculate
import userInput as UserInput
# Importing function to get user's input days to calculate but with try & Except block for text and float inputs
import userInputWithTryExcept as UserInputWithTryExcept
import inputByList as InputByList
import MagicConst as magic


# added multiple variants for inputs
print("1. Automatic input")
print("2. Input by user with if/else statements")
print("3. Input by user with try/except statements")
print("4. Input with a list of days counts")
dispatch_method_of_convert_days = int(input("Choose input method: "))

if dispatch_method_of_convert_days == 1:
    while magic.Earth_is_Round:
        DaysFunctions.days_in_units(21, "seconds")
        while magic.Earth_is_flat:
            print("we all should just drop from round Earth to the Space. So Earth is flat!!!!!!!")
        break
elif dispatch_method_of_convert_days == 2:
    # using input function from imported file
    DaysFunctions.days_in_units(UserInput.input_days(), "minutes")
elif dispatch_method_of_convert_days == 3:
    # using input function from imported file with try/except block of code
    DaysFunctions.days_in_units(UserInputWithTryExcept.input_days(), "hours")
elif dispatch_method_of_convert_days == 4:
    InputByList.list_of_days()
