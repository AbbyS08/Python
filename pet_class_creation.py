# Pet Class Creation and Exploration

class Pet:
    def __init__(self, kind, breed, name):
        # Instance Variables for objects
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter methods
    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
        
    def get_name(self):
        return self.__name
    
    # Setter Methods
    def set_kind(self, value):
        self.__kind = value
    
    def set_breed(self, value):
        self.__breed = value

    def set_name(self, value):
        self.__name = value
    
    # Method to print pet details
    def print_details(self):
        print(f"Pet Details: {self.__dict__}")

def main():
    # Creating three pet objects
    pet1 = Pet("Cat", "American Shorthair", "Midna")
    pet2 = Pet("Dog", "Labrador", "Mollie")
    pet3 = Pet("Snake", "Boa Constrictor", "Henry")

    # Printing details for each pet
    pet1.print_details()
    pet2.print_details()
    pet3.print_details()

    # Three Special Methods/Functions: __name__, __bases__, isinstance()
    # __name__ returns the class name as a string
    print(Pet.__name__)
    # __bases__ shows the superclasses of a class, or object if there are none
    print(Pet.__bases__)
    # isinstance checks if the object is part of a class
    print(isinstance(pet1, Pet))
    # Using isinstance in code
    if isinstance(pet1, Pet):
        print("pet1 is part of the Pet class")

main()

