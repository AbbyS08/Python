# Personal Diary

def main():

    # Asking the user for a date, time, and diary entry
    date = input("Enter date: ")
    time = input("Enter time: ")
    entry = input("Enter diary entry: ")

    # Creating the file in append mode
    with open('8/diary/diary.txt', 'a') as file:  
        # Writing the three things inputted to the diary.txt file
        file.write(date + ', ' + time + '\n'+ entry +'\n')
    file.close()

main()