# Inheritance Using Employee Classes

class Employee:
    def __init__(self, name, number):
        # Instance variables for employee name and number
        self.__employee_name = name
        self.__employee_number = number
    
    # Getter Methods
    def get_employee_name(self):
        return self.__employee_name
    
    def get_employee_number(self):
        return self.__employee_number
    
    # Setter Methods
    def set_employee_name(self, value):
        self.__employee_name = value

    def set_employee_number(self, value):
        self.__employee_number = value

class ProductionWorker(Employee):
    def __init__(self, shift_number, hourly_pay_rate):
        # Inheriting the instance variables from the superclass Employee
        super().__init__(name = "name", number = "number") # Using default values as filler variables
        # Creating instance variables specific to the ProductionWorker class
        self.__shift_number = shift_number # 1 is day, 2 is night
        self.__hourly_pay_rate = hourly_pay_rate

    # Getter Methods
    def get_shift_number(self):
        return self.__shift_number
    
    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate
    
    # Setter Methods
    def set_shift_number(self, value):
        self.__shift_number = value

    def set_hourly_pay_rate(self, value):
        self.__hourly_pay_rate = value

def main():
    try:
        # Creating an object using the ProductionWorker class
        worker = ProductionWorker("0", "0") # Filler variables
        # Asking the user for employee details
        print("-Enter Employee Details-")
        worker.set_employee_name(input("Enter the Employee Name: "))
        worker.set_employee_number(input("Enter the Employee Number: "))
        worker.set_hourly_pay_rate(float(input("Enter the employee's Hourly Pay Rate: ")))
        worker.set_shift_number(int(input("Enter the employee's Shift Number (1 is day, 2 is night): ")))
        # Determining if the shift is night or day based on the inputted shift number
        if worker._ProductionWorker__shift_number == 1:
            worker_shift = "Day"
        elif worker._ProductionWorker__shift_number ==2:
            worker_shift = "Night"
        else:
            worker_shift = "Invalid Input"
        # Printing the employee information
        print(f"""Employee Details: 
Name: {worker.get_employee_name()}
Number: {worker.get_employee_number()}
Shift: {worker_shift}
Hourly Pay Rate: {worker.get_hourly_pay_rate():.2f}""")
    # Error messages
    except ValueError:
        print("The input for shift number or/and hourly pay rate is/are invalid.")
    except:
        print("Something went wrong.")


main()