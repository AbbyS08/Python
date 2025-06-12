# Steps Each Day Calculator
# Creating two lists
days = ["Sunday", "Monday", "Tuesday",
        "Wednesday", "Thursday", "Friday", "Saturday"]
steps = []
# Asking for the amount of steps each day
for day in days:
    steps.append(int(input(f"How many steps did you take on {day}? ")))
# Printing the amount of steps taken each day
for i in range(len(days)):
    step = steps[i]
    next_day = days[i]
    print(f"You took {step} steps on {next_day}.")
# Calculating and printing the total number of steps
total_steps = 0
for p in steps:
    total_steps += p
print(f"Total Steps: {total_steps}")
# Calculating and printing the average number of steps
average_steps = total_steps // 7
print(f"Average Steps: {average_steps}")
