# Program using classes and objects to save pet info

class Pet:
    # Class Variable
    vet_name = "Domestic Pets Veterinary Office"
    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type = "Dog"):
        # Instance Variables for objects
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter methods
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
        
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type

    # Setter Methods
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
    
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value

    def set_pet_type(self, value):
        self.__pet_type = value

    # Method to print pet and owner details
    def display_pet_info(self):
        print(f"Pet and Owner Details: {self.__dict__}")

# Function checking if an object has a property
def check_property(pet, property):
    print(hasattr(pet, property))



def main():
    # Making three pets
    pet1 = Pet("Abby", "Standish", 1234, "Joan", "Cat")
    pet2 = Pet("Ben", "Standish", 5678, "Cocoa")
    pet3 = Pet("Lia", "Standish", 1357, "Mollie")
    # Setting pet2 with different attributes
    pet2.set_owner_first_name("Sue")
    pet2.set_owner_last_name("Anderson")
    pet2.set_pet_id(9999)
    pet2.set_pet_name("Cocoa_The_Destroyer")
    pet2.set_pet_type("Destructive_Dog")
    # Displaying info for the three pets
    pet1.display_pet_info()
    pet2.display_pet_info()
    pet3.display_pet_info()
    # Three examples of checking properties
    check_property(pet1, "_Pet__pet_type")
    check_property(pet2, "_Pet__pet_id")
    check_property(pet3, "_Pet__owner_last_name")
    # Two more examples of using display_pet_info()
    pet4 = Pet("Samuel", "Standish", 7898, "Kira", "Cat")
    pet4.display_pet_info()
    pet5 = Pet("Susan", "Standish", 2354, "Riley")
    pet5.display_pet_info()

main()