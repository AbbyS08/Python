# Daily Heart Rate Tracker
# Creating a time list and an empty list for storage
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []
# Asking to input heart rate for each time of day
for time in time_slots:
    if time != "Midday":
        heart_rate = float(
            input(f"Enter your heart rate (in BPM) in the {time}: "))
    else:
        heart_rate = float(
            input(f"Enter your heart rate (in BPM) at {time}: "))
    # Adding time and heart rate to the list heart_rates
    heart_rates.append([time, heart_rate])
# Finding the total of the heart rates for the average
total = 0
for i in range(len(heart_rates)):
    total += heart_rates[i][1]
# Calculating and printing the average heart rate
average = total/len(heart_rates)
print(f"Average heart rate today: {average:.2f} BPM")
