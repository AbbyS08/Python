# Budget Breakdown Calculator Project
# Asking for net monthly income
total = float(input("What is your net monthly income?: $"))
# Asking for the amount spent in a month for different categories
print("How much do you spend in a month on each category?")
housing = float(input("Housing (rent or mortgage): $"))
utilities = float(input("Utilities: $"))
groceries = float(input("Groceries: $"))
transportation = float(input("Transportation: $"))
health_care = float(input("Health Care: $"))
personal_care = float(input("Personal Care: $"))
clothing = float(input("Clothing: $"))
debt = float(input("Debt: $"))
# Calculating the total amount spent and the amount of money left
total_spent = housing+utilities+groceries + \
    transportation+health_care+personal_care+clothing+debt
money_left = total-total_spent
# Calculating the percentage of total budget spent in each category in decimal form
housing /= total
utilities /= total
groceries /= total
transportation /= total
health_care /= total
personal_care /= total
clothing /= total
debt /= total
# Printing the total spent and money left
print(f"Total Amount Spent: ${total_spent:.2f}",
      f"\nMoney Left: ${money_left:.2f}")
# Printing the results for each individual category, changing to percent form, and rounding the percents to whole numbers
print("Percent of how much of the total budget is spent in each category")
print(f"Housing: {housing*100:.0f}%", f"Utilities: {utilities*100:.0f}%",
      f"Groceries: {groceries*100:.0f}%", f"Transportation: {transportation*100:.0f}%",
      f"Health Care: {health_care*100:.0f}%", f"Personal Care: {personal_care*100:.0f}%", f"Clothing: {clothing*100:.0f}%", f"Debt: {debt*100:.0f}%", sep="\n")
# A list of percents with the category names is shown
