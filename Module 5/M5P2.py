# Christopher Monarre M5P2

# Variables
item = str(input("Enter Item (A or B): "))
quantity = int(input("Enter quantity: "))
unit_price = 0



# Calculations

# if/else statement for unit price
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

extended_price = quantity * unit_price



# Display
print("Item: ", item)
print("Unit Price: ", unit_price)
print("Extended Price: ", extended_price)
