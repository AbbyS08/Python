# Making comparisons between 2 integers using logical operators
# Asking for 2 integers to compare
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
# And comparisons
if first > 0 and second > 0:
    print("Both numbers are positive and not 0: True")
else:
    print("Both numbers are positive and not 0: False")
if first == 0 and second == 0:
    print("Both numbers are 0: True")
else:
    print("Both numbers are 0: False")
# Or comparisons
if first < 10 or second < 10:
    print("Either number or both numbers is less than 10: True")
else:
    print("Either number is less than 10: False")
if first - 5 == 0 or second - 5 == 0:
    print("One number is 5: True")
else:
    print("One number is 5: False")
# Not comparisons
if not first != second:
    print("Both numbers are the same number: True")
else:
    print("Both numbers are the same number: False")
if not first > second:
    print("The first number is not greater than the second: True")
else:
    print("The first number is not greater than the second: False")
