# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime

def main():
   
    print("\n\n")
    try:
        # Using the today method as part of datetime module 
        today = datetime.today()
        # Asking the user for their birthday
        birth_year = int(input("What year were you born?  "))
        month = int(input("What Month were you born (as a number. May would be 5)  "))
        day = int(input("What day of the month were you born?  "))
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        # Creating a birthday object from the datetime class
        birthday = datetime(birth_year, month, day)
        # Printing the birthday formatted with the strftime method
        print("Your birthday is: ")
        birthday_output = birthday.strftime("%Y-%m-%d")
        print(birthday_output) 
        # Calculating the years old, printing the rounded result by using floor division
        delta = today - birthday
        print(f'Difference is {delta.days} days')
        delta_years = delta.days // 365.2425
       
        print(f'You are {delta_years} years old')


        # Finding the real (not rounded) amount of years
        real_delta_years = delta.days / 365.2425
        # Calculating the amount of months old based on the real years
        delta_months = (real_delta_years*12) 
        print(f"You are {delta_months:.1f} months old.")

        # Getting the amount of days old, then dividing by 7 to get amount of weeks old
        days = delta.days
        weeks = days/7
        print(f"You are {weeks:.0f} weeks old.")

       

      
    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()