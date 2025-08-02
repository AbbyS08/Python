# Creating a custom calendar program
import calendar
import datetime

def main():
    try:
        # Finding the current year
        current_year = datetime.datetime.now().year
        # Asking the user for their birth month
        birth_month = int(input("Please enter your birth month as a number: "))
        # Making sure the birth month input is a month number
        if birth_month >= 1 and birth_month <= 12:
            # Printing calendar based on current year and birth month
            print(calendar.month(current_year, birth_month))
        else:
            print("The birth month number must be between 1 and 12.")
    # Error Messages
    except ValueError:
        print("Input a number between 1 and 12.")
    except:
        print("Something went wrong.")


main()