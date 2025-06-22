# Factorial Calculator
# Function calculating the factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    if n > 1:
        # Recursive, finds the product of all numbers before
        return n * factorial(n-1)


# The main function gets a number from the user, then prints the result of factorial() with the number
def main():
    number = int(input("Enter a non-negative integer: "))
    print(factorial(number))


main()
