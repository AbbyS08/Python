from math_operations import calculator
from math_operations import geometry


result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

result = calculator.add(7, 2)
print("Result:", result)

area = geometry.area_of_square(8)
print(f"Area of square: {area:.2f}")

area = geometry.area_of_circle(3)
print(f"Area of circle: {area:.2f}")

area = geometry.area_of_rectangle(3, 4)
print(f"Area of rectangle: {area:.2f}")

area = geometry.area_of_triangle(5, 7)
print(f"Area of triangle: {area:.2f}")
