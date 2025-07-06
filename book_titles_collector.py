# Book Titles Collector
# Program that asks for 10 book titles and sorts them into a list


def main():
    try:
        # Creating the list that holds the titles and a counter
        books = []
        counter = 0
        # Asking for 10 book titles and adding them to the books list
        while counter < 10:
            counter += 1
            books.append(input(f"Enter book title {counter}: ").title())
        # Creating a new list with the sorted book titles
        books_sorted = sorted(books)
        # Printing the sorted book titles on separate lines
        for book in books_sorted:
            print(book)
    except:
        print("\nSomething went wrong. Please try again.")


main()
