# Final - CRUD Sample


def main_menu():
    print("Menu:")
    # Using choice to enter the loop
    choice = 0
    # Exiting the loop if a valid number is entered
    while not(1 <= choice <= 5):
        try:
            # Displaying 5 options in the menu
            print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            # Asking the user to input a number
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")
        except:
            print("\nSomething went wrong.")

def check():
        try:
            # Opening the file in read mode
            file = open("customer_list.txt", 'r')
            # Taking all the lines from the file, then closing it
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError:
            # Making a new file if it doesn't already exist
            print("Customer list does not exist. Creating a new file...")
            return []

def create():
        try:
            # Using check to get a list to add the entry to
            customer = check()
            # Asking for entry info to input
            fname = input("Please enter the customer\'s first name: ")
            lname = input("Please enter the customer\'s last name: ")
            phone = input("Please enter the customer\'s phone: ")
            email = input("Please enter the customer\'s email: ")
            # Creating the entry using the inputted info
            entry = f"{fname}, {lname}, {phone}, {email}"
            # Adding the entry to the customer list
            customer.append(entry)
            # Saving th entry to the file
            save(customer)
        except Exception as e:
            print("Something went wrong.",e)

def save(output):
    try:
        # Opening the file in write mode
        file = open("customer_list.txt", 'w')
        # Writing each line to the file
        for line in output:
            file.write(line)
            file.write("\n")
        # Closing the file
        file.close()
        print("File updated.")
    except Exception as e:
        print("Something went wrong.",e)

def read():
    try:
        # Asking for the last name
        search_term = input("Please enter the last name of who you are looking for: ")
        # Assigning the lines of the file to customer
        customer = check()
        while customer.count != 0: # Source: my Dad helped me with this function
            # Making entry global so string methods can be used on it
            global entry
            # Printing the entry of the customer that matches the search term
            entry = customer.pop()
            if search_term in entry:
                print(entry)
                break
            else:
                print("Entry not found.")
    except IndexError:
        print("There are no entries in the list.")
    except Exception as e:
        print(f"Something went wrong. {e}")

def update():
    try:
        # Using read to display the entry
        read()
        # Getting what the user wants to change and the new value
        replacement = input("Enter value you want to change: ")
        change = input("Enter the new value: ")
        # Using replace to change the entry
        updated_entry = entry.replace(replacement, change, 1)
        # Saving the updated entry
        save(updated_entry)
    except Exception as e:
        print(f"Something went wrong. {e}")

    

def delete():
    try:
        # Displaying the entry 
        read()
        # Asking the user if they want to delete the displayed entry
        confirmation = input("Do you want to delete this entry? (yes or no): ")
        if confirmation.lower() == "yes":
            # Replacing the entry with nothing to delete it, then saving the empty line
            updated = entry.replace(entry, "")
            save(updated)
        elif confirmation.lower() =="no":
            # Not deleting the entry if the answer is no
            print("Entry not deleted.")
        else:
            # Message if something other than yes or no is entered
            print("Confirmation input invalid. Entry not deleted.")
    except Exception as e:
        print(f"Something went wrong. {e}")

def main():
    try:
        choice = 0
        # Quitting if the choice is 5, else going to the function for each choice
        while choice != 5:
            choice = main_menu()
            if choice == 1:
                create()
            elif choice == 2:
                read()
            elif choice == 3:
                update()
            elif choice == 4:
                delete()
        print("\nData saved as customer_list.txt\n")
    except Exception as e:
        print(f"Something went wrong. {e}")


main()


