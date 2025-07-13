# Color Combination Mini Quiz

def main():
    print("Welcome to the color combination quiz! \nEnter the answer number to select your answer.")
    try:
        # Creating counters for correct and incorrect answers
        correct_answers = 0
        incorrect_answers = 0
        total_questions = 5
        # Reusable answer choices
        rb = "Red and Blue"
        by = "Blue and Yellow"
        ry = "Red and Yellow"
        rw = "Red and White"
        bg = "Blue and Green"
        pw = "Purple and White"
        # Starting the quiz questions
        print(f"\nQ1 Which two colors combine to make green?\n1.{rb}\n2.{by}\n3.{ry}")
        # Asking for a number input for the answer
        guess = int(input("Enter the number of the answer: "))
        correct_answer1 = 2
        # Checking if the inputted answer was one of the options
        if guess == 1 or guess == 2 or guess == 3:
            # Printing a correct or incorrect message based on the answer, and adding to the counters
            if guess != correct_answer1:
                print(f"Wrong! The correct answer is {correct_answer1}")
                incorrect_answers += 1
            elif guess == correct_answer1:
                print("Correct Answer!")
                correct_answers += 1
        else:
            print(f"That's not an option! The correct answer is {correct_answer1}")
            incorrect_answers += 1
        # Question 2
        print(f"\nQ2 Which two colors combine to make purple?\n1.{rb}\n2.{by}\n3.{ry}")
        guess = int(input("Enter the number of the answer: "))
        correct_answer2 = 1
        if guess == 1 or guess == 2 or guess == 3:
            if guess != correct_answer2:
                print(f"Wrong! The correct answer is {correct_answer2}")
                incorrect_answers += 1
            elif guess == correct_answer2:
                print("Correct Answer!")
                correct_answers += 1
        else:
            print(f"That's not an option! The correct answer is {correct_answer2}")
            incorrect_answers += 1
        # Question 3
        print(f"\nQ3 Which two colors combine to make orange?\n1.{rb}\n2.{by}\n3.{ry}")
        guess = int(input("Enter the number of the answer: "))
        correct_answer3 = 3
        if guess == 1 or guess == 2 or guess == 3:
            if guess != correct_answer3:
                print(f"Wrong! The correct answer is {correct_answer3}")
                incorrect_answers += 1
            elif guess == correct_answer3:
                print("Correct Answer!")
                correct_answers += 1
        else:
            print(f"That's not an option! The correct answer is {correct_answer3}")
            incorrect_answers += 1
        # Question 4
        print(f"\nQ4 Which two colors combine to make pink?\n1.{rw}\n2.{bg}\n3.{pw}")
        guess = int(input("Enter the number of the answer: "))
        correct_answer4 = 1
        if guess == 1 or guess == 2 or guess == 3:
            if guess != correct_answer4:
                print(f"Wrong! The correct answer is {correct_answer4}")
                incorrect_answers += 1
            elif guess == correct_answer4:
                print("Correct Answer!")
                correct_answers += 1
        else:
            print(f"That's not an option! The correct answer is {correct_answer4}")
            incorrect_answers += 1
        # Question 5 
        print(f"\nQ5 Which two colors combine to make lavender?\n1.{rw}\n2.{bg}\n3.{pw}")
        guess = int(input("Enter the number of the answer: "))
        correct_answer5 = 3
        if guess == 1 or guess == 2 or guess == 3:
            if guess != correct_answer5:
                print(f"Wrong! The correct answer is {correct_answer5}")
                incorrect_answers += 1
            elif guess == correct_answer5:
                print("Correct Answer!")
                correct_answers += 1
        else:
            print(f"That's not an option! The correct answer is {correct_answer5}")
            incorrect_answers += 1
        # Telling the user that they are finished, their amount of correct and incorrect answers, and accuracy
        print(f"""\nCongratulations! You finished the quiz!
You had {correct_answers} correct answers and {incorrect_answers} incorrect answers.
Accuracy: {(correct_answers/total_questions)*100:.0f}%""")
    # Exception for if an integer is not entered
    except ValueError:
        print("Only integer numbers can be entered. Please restart the quiz.")
    # Exception for if the user tries to copy the question 
    except KeyboardInterrupt:
        print("Ctrl + C ends the quiz. Please restart.")
    # Generic exception message 
    except:
        print("Something went wrong. Please restart the quiz.")

main()