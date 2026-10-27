# Christopher Monarrez M5P1

# Variables
item_quantity = int(input("Enter quantity of items: "))


# Calculations
if item_quantity >= 1000:
    unit_price = 3
else:
    unit_price = 5

extended_price = item_quantity * unit_price
tax = extended_price * .07
total = extended_price + tax

# Display
print("Quantity: ", item_quantity)
print("Unit Price: ", unit_price)
print("Extended Price: ", extended_price)
print("Tax", tax)
print("Total: ", total)