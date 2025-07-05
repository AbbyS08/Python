# ASCII Value Finder

def main():
    try:
        # Asking the user for a character
        character_from_user = input("Enter a single character: ")
        # Printing the ASCII value of the character if there is only 1 character
        if len(character_from_user) == 1:
            ascii_value = ord(character_from_user)
            print(ascii_value)
        else:
            print("Only one character can be entered.")
        try:
            # Asking the user for an ASCII value
            ascii_from_user = int(input("Enter an ASCII value: "))
            # Printing the ASCII value if it is between 32 and 127
            if ascii_from_user >= 32 and ascii_from_user <= 127:
                character = chr(ascii_from_user)
                print(character)
            else:
                print("The ASCII value entered must be a number between 32 and 127.")
        except:
            print("The ASCII value entered must be a number between 32 and 127.")
    except:
        print("\nSomething went wrong. Please try again.")


main()
