from datetime import datetime


goal = input("Enter your goal with a deadline separated by colon\n").split(":")
today = datetime.date(datetime.today())
deadline_date = ""
try:
    deadline_date = datetime.date(datetime.strptime(goal[1], "%d.%m.%Y"))
except ValueError:
    print("It's not a date")
    exit()
if deadline_date < today:
    print(f"You can't bring back the past. You won't done your goal {(deadline_date-today).days} days ago...")
else:
    print(f"Dear user! Time remaining for you goal: {goal[0]} is {(deadline_date-today).days} days.")
