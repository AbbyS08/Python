# Program that gives the letter grade earned based on the numeric grade
# Asking the user for the numeric grade
num_grade = float(input("Enter the numeric grade: "))
# Checking if the numeric grade is above 100, exiting if it is
if num_grade > 100:
    print("The numeric grade must be between 0 and 100.")
    exit()
# Assigning the letter grade based on the numeric grade entered
elif num_grade >= 90:
    letter_grade = "A"
elif num_grade >= 80:
    letter_grade = "B"
elif num_grade >= 70:
    letter_grade = "C"
elif num_grade >= 60:
    letter_grade = "D"
elif num_grade >= 0:
    letter_grade = "F"
# Checking if the numeric grade is below 0, exiting if it is
else:
    print("The numeric grade must be between 0 and 100.")
    exit()
# Printing the letter grade to the user
print(f"The letter grade is: {letter_grade}")
