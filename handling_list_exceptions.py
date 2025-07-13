# Handling List Exceptions

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    try:
        # Asking for an index and artist name
        index = int(input("Enter the index of the artist to replace: "))
        new_name = input("Enter the new artist name: ")
        # Replacing the artist at the index
        top_artists[index] = new_name
        # Printing the new list
        print(f"Updated list: {top_artists}")
    # Error messages
    except (ValueError, IndexError):
        print("An input error occurred.")
    except:
        print("Something went wrong.")


main()
