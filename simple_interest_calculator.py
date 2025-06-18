# Simple Interest Calculator

def main():
    # Asking for the principal, rate, and time
    input_principal = float(input("Enter the principal amount: $"))
    input_rate = float(input("Enter the interest rate: "))
    input_time = float(input("Enter the time in years: "))
    # Assigning the result of calculate_interest function to x
    x = calculate_interest(input_principal, input_rate, input_time)
    # Printing the inputted values and the calculated interest
    print(
        f"The simple interest for ${input_principal:,.2f} at {input_rate}% over {input_time} years is ${x:,.2f}.")


# Function that uses the inputted values to calculate simple interest
def calculate_interest(principal, rate, time):
    calculated_interest = (principal * rate * time) / 100
    return calculated_interest


# Calling the main function
main()
