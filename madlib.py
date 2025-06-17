# Madlib based on the Itsy Bitsy Spider song

# Making a function to play the song
def custom_song(adjective1, adjective2, animal, noun1, noun2, verb1, noun3, verb2):
    print(f"\nThe {adjective1} {adjective2} {animal} went up the {noun1}")
    print(f"Down came the {noun2}, and {verb1} the {animal} out")
    print(f"Out came the {noun3}, and {verb2} up all the {noun2}")
    print(
        f"And the {adjective1} {adjective2} {animal} went up the {noun1} again")


# Asking for 8 words to input into the song
animal_input = input("Enter an animal: ")
adj1_input = input("Enter an adjective: ")
adj2_input = input("Enter an adjective: ")
noun1_input = input("Enter a noun: ")
noun2_input = input("Enter a noun: ")
noun3_input = input("Enter a noun: ")
verb1_input = input("Enter a verb (past tense): ")
verb2_input = input("Enter a verb (past tense): ")

# Calling the custom_song function
custom_song(adjective1=adj1_input, adjective2=adj2_input, animal=animal_input, noun1=noun1_input,
            noun2=noun2_input, verb1=verb1_input, noun3=noun3_input, verb2=verb2_input)
