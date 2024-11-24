# Description: Write a program that asks the user to enter two numbers and then prints the maximum of the two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

max_num = num1 if num1 > num2 else num2

print(f"The maximum of {num1} and {num2} is{max_num}")