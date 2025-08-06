


def main_menu():
    print("Menu:")
    choice = 0
    while not(1 <= choice <= 5):
        try:
            print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
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
            file = open("customer_list.txt", 'r')
            lines = file.readlines()
            file.close()
            return lines
        except FileNotFoundError:
            print("Customer list does not exist. Creating a new file...")
            return []

def create():
        customer = check()
        fname = input("Please enter the customer\'s first name: ")
        lname = input("Please enter the customer\'s last name: ")
        phone = input("Please enter the customer\'s phone: ")
        email = input("Please enter the customer\'s email: ")
        entry = f"{fname}, {lname}, {phone}, {email}"
        customer.append(entry)
        save(customer)

def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

def read():
    try:
        search_term = input("Please enter the last name of who you are looking for: ")
        customer = check()
        while customer.count != 0: # Source: my Dad helped me with this function
            global entry
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
        read()
        replacement = input("Enter value you want to change: ")
        change = input("Enter the new value: ")
        updated_entry = entry.replace(replacement, change, 1)
        save(updated_entry)
    except Exception as e:
        print(f"Something went wrong. {e}")

    

def delete():
    try:
        read()
        confirmation = input("Do you want to delete this entry? (yes or no): ")
        if confirmation.lower() == "yes":
            updated = entry.replace(entry, "")
            save(updated)
        elif confirmation.lower() =="no":
            print("Entry not deleted.")
        else:
            print("Confirmation input invalid. Entry not deleted.")
    except Exception as e:
        print(f"Something went wrong. {e}")

def main():
    try:
        choice = 0
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


