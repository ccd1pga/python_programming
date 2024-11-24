# Write a program that calculates the distance between two points (x1, y1) and (x2, y2). All numbers and return values should be rounded to two decimal places.
x1, y1 = 3, 4
x2, y2 = 6, 8

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")
