# This program says what someone can do based on how old they are
# Asking for age
age = int(input("What is your age?: "))
# Checking if the age is high enough to do activities, printing results in a list
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")
if age >= 18:
    print("You can vote.")
else:
    print("You are not old enough to vote.")
if age >= 21:
    print("You can legally buy alcohol.")
else:
    print("You cannot legally buy alcohol.")
if age >= 65:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")
