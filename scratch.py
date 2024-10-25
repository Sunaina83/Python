#1 Name and Welcome

Name= input("Enter your name: ")
print(f"Hello  {Name}")

#2 Radius of a circle and the prints out the area of the circle.

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is {area}")

#3 Length and width of a rectangle

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

r_area = length * width

perimeter = 2 * (length + width)

print(f"The area of the rectangle is {r_area:.2f}")
print(f"The perimeter of the rectangle is {perimeter:.2f}")

#4  three integer numbers. The program prints out the sum, product, and average of the numbers.

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3

# Print the results
print(f"The sum of the numbers is: {sum}")
print(f"The product of the numbers is: {product}")
print(f"The average of the numbers is: {average:.2f}")

#5 medieval units: talents, pounds , and lots
LOT= 13.3
POUND = 32
TALENT = 20


talent = int(input("Enter the number of talents: "))
pound = int(input("Enter the number of pounds: "))
lot = int(input("Enter the number of lots: "))

total_grams = (talent * TALENT * POUND * LOT) + (pound * POUND * LOT) + (lot * LOT)

kg = int(total_grams // 1000)
remaining_grams = total_grams % 1000
print(f"The total mass is {kg} kilograms and {remaining_grams:.1f} grams.")

