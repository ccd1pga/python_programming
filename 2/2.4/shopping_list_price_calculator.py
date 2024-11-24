# Difficulty: Easy
item1 = 4.99
item2 = 2.75
item3 = 1.25

total_price = item1 + item2 + item3
formatted_total = round(total_price, 1) # error in book, should be 1 instead of 2, to show how the round function works.

print(f"The total price of the items is ${formatted_total}")