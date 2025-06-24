# NATO Phonetic Alphabet Dictionary
# Source for nato alphabet: https://securityjournaluk.com/nato-phonetic-alphabet/#:~:text=B%3A%20Bravo%20(BRAH%2Dvoh,Delta%20(DELL%2Dtah)
# Creating the dictionary
nato_alphabet = {
    "a": "alpha",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliet",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "x-ray",
    "y": "yankee",
    "z": "zulu"
}


# Asking for a word and printing the nato alphabet word for each letter
def main():
    word = input("Enter a word: ")
    word = word.lower()  # Changing to lowercase so the keys work
    for letter in word:
        print(nato_alphabet[letter])


main()
