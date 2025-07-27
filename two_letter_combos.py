# Using a generator function to create 2 letter combinations 

def two_letter_combinations(character_list):
    # The double for loop grabs all the letters for each letter
    for letter1 in character_list:
        for letter2 in character_list:
            # Yielding the letters combined together
            yield letter1 + letter2


def main():
    # Creating the 5 character list to use in the generator
    five_character_list = ["v", "w", "x", "y", "z"]
    # Making a variable to store the result
    result = two_letter_combinations(five_character_list)
    # Iterating over the generator to print each combination
    for combo in result:
        print(combo, end= " ")
        


main()