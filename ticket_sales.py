# Program that does ticket sales for seats
# List of all the seats
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
selected_seat = 1  # Starting the loop
while selected_seat != 0:
    # Printing available seats
    print(f"Possible seats: {seats}")
    # Asking the user to select a seat
    selected_seat = int(
        input("Select a seat by entering its number, 0 ends the purchase process: "))
    # Removing the seat selected if it is in the seats list
    if selected_seat in seats:
        seats.remove(selected_seat)
    # Using 0 to break out of the loop and end the purchase process
    elif selected_seat == 0:
        break
    # If the number is not in the seats list, printing an error message
    else:
        print(f"{selected_seat} is not an available seat. Please try again.")
    # Checking to see if there are any seats left, breaking the loop if there are none left
    if len(seats) == 0:
        print("There are no available seats.")
        break
