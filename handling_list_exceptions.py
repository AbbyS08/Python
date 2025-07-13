# Handling List Exceptions

def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    try:
        index = int(input("Enter the index of the artist to replace: "))
        new_name = input("Enter the new artist name: ")
        top_artists[index] = new_name
        print(f"Updated list: {top_artists}")
    
    except (ValueError, IndexError):
        print("An input error occurred.")
    except:
        print("Something went wrong.")


main()