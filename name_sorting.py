# Name Sorting Program
# Creating an empty list to put names into
names = []
# Asking for five names and changing them to lowercase
for i in range(5):
    names.append(input(f"Enter name {i + 1}: "))
names = [name.lower() for name in names]

# Bubble sorting
swapped = True
while swapped:
    swapped = False
    for l in range(len(names) - 1):
        if names[l] > names[l + 1]:
            names[l], names[l + 1] = names[l + 1], names[l]
            swapped = True
# Printing sorted list
print(f"Sorted name list: {names}")
# Printing reversed list
names.reverse()
print(f"Reversed name list: {names}")
