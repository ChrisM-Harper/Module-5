# Christopher Monarrez M5P3

# Variables 
number_of_books = int(input("Enter Number of Books: "))
cost_per_book = float(input("Enter Cost per Book: "))
total_cost = number_of_books * cost_per_book
shipping_cost = 0

# Calculations
if total_cost <= 50:
    shipping_cost = 25
else:
    shipping_cost = 0

# Display
print("Total Order Cost: $", total_cost)
print("Shipping fee: $", shipping_cost)
