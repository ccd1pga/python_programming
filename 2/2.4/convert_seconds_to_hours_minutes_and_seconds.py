
total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60 # % 3600 is the remainder of total_seconds divided by 3600, so % is the modulo operator
seconds = total_seconds % 60

print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds.")
