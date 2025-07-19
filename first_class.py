# Creating a Person class

class Person:
    # Using 4 different variables to hold the info of each person
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
        
    # Accessor functions used to access the object's attributes
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
    # Mutator functions to change the object's attributes
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

def main():
    try:
        # Creating 3 different objects using the Person class
        person1 = Person("Abby", "111Street1", 16, "111-111-1111")
        person2 = Person("Lia", "222Street2", 14, "222-222-2222")
        person3 = Person("Katie", "333Street3", 8, "333-333-3333")
        # Printing the attributes for the 3 objects using the accessor functions
        print(f"""Person 1: Name - {person1.get_name()}
Address - {person1.get_address()}
Age - {person1.get_age()}
Phone Number - {person1.get_phone_number()}\n
Person 2: Name - {person2.get_name()}
Address - {person2.get_address()}
Age - {person2.get_age()}
Phone Number - {person2.get_phone_number()}\n
Person 3: Name - {person3.get_name()}
Address - {person3.get_address()}
Age - {person3.get_age()}
Phone Number - {person3.get_phone_number()}
""")

    except:
        print("Something went wrong.")


main()