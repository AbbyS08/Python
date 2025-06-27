# Number Guessing Game
# Importing the random module
import random


def main():
    # Creating the random number
    random_number = random.randrange(1, 101)
    while True:
        try:
            # Asking for an integer number from the user
            number_guess = int(
                input("Please enter a integer number between 1 and 100: "))
            # If statement to make sure the guessed number is in range
            if number_guess >= 1 and number_guess <= 100:
                # If statement to tell the user how close their guess is to the random number
                if abs(number_guess - random_number) == 0:
                    print("You guessed the correct number!")
                    # Breaking out of the loop if the random number is correctly guessed
                    break
                elif abs(number_guess - random_number) <= 5:
                    print("Very Hot")
                elif abs(number_guess - random_number) <= 15:
                    print("Hot")
                elif abs(number_guess - random_number) <= 25:
                    print("Cool")
                else:
                    print("Cold")
            else:
                print("The guessed number needs to be between 1 and 100.")
        # Printing an error message if the input is not an integer
        except:
            print("Invalid input. Please try again.")


main()
