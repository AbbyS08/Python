# Simple Python program to calculate the square of a number

def square_number():
    try:
        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")
    except ValueError:
        print("Please enter a valid integer number")
    except:
        print("\nSomething went wrong. Please try again.")


square_number()
