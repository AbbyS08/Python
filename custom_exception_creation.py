# Creating a Custom Exception

class NotNumericError(Exception):
    # Custom exception to raise if a number is not numeric
    def __init__(self, message):
        self.message = message

def main():
    input_is_valid = False # Flag
    while not input_is_valid:
        try:
            # Asking for a number
            number_input = input("Enter a number: ")
            # Raising the custom exception if the input isn't a number
            if not number_input.isnumeric():
                raise NotNumericError("The input is not a number.")
        # Error message
        except NotNumericError as e:
            print(f"Caught an error: {e.message}")
        # Printing confirmation message if the input is valid
        else:
            print(f"Input is valid: {number_input}")
            input_is_valid = True # Changing the flag if the loop should be exited
        finally:
            print("End of program execution.")

main()
