# Description: Write a Python program which accepts the radius of a circle from the user and compute the area and circumference.
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"The area of a circle with radius {radius} is {area:.2f}\n and the circumference is {circumference:.2f}.")   # \n line break, :.2f format to 2 decimal places
