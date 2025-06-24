# Using Tuples
# Creating a tuple
programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials',
                       'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')


# Printing each item in the tuple and the length of the tuple
def main():
    for programming_class in programming_classes:
        print(programming_class)
    print(len(programming_classes), "classes")


main()
