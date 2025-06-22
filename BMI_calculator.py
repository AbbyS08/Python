# BMI Calculator
# Global conversion variables
LB_TO_KG = 0.453592  # 1lb = 0.453592kg
IN_TO_M = 0.0254  # 1in = 0.0254m


def main():
    # Asking the user for height and weight
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))
    # Converting into metric
    height = height * IN_TO_M
    weight = weight * LB_TO_KG
    # Calculating bmi value
    bmi = weight / (height * height)
    # Finding BMI category
    # Source: https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html
    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "healthy"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obesity"
    # Printing the BMI and category
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the {category} weight category.")


main()
