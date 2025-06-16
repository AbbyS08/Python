# Area Calculator
# Function to calculate and print the area of a square
def square(side):
    area_square = side*side
    print(f"The area of the square is {area_square:.2f} square units.")


# Function to calculate and print the area of a circle
def circle(radius):
    area_circle = 3.14*radius*radius
    print(f"The area of the circle is {area_circle:.2f} square units.")


# Calling the square and circle functions
square(float(input("Input the side length of a square: ")))

circle(float(input("Input the radius of a circle: ")))
