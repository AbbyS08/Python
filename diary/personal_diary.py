# Personal Diary
import os

def main():

    # Asking the user for a date, time, and diary entry
    try:
        date = input("Enter date: ")
        time = input("Enter time: ")
        entry = input("Enter diary entry: ")
        #ensure that the directory exists already
        os.makedirs("8/diary",exist_ok=True)
        # Creating the file in append mode
        with open('8/diary/diary.txt', 'a') as file:  
            # Writing the three things inputted to the diary.txt file
            file.write(date + ', ' + time + '\n'+ entry +'\n')
        file.close()
    except FileNotFoundError:
        print("File not found.")
    except:
        print("Something went wrong.")

main()
