# Write a program that takes three numbers as input and calculates the average of the three numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print(f"The average of {num1}, {num2}, and {num3} is {average:.2f}")