# Christopher Monarrez M5P4

# Variables
name_of_appliance = str(input("Enter Name of Appliance: "))
cost_of_appliance = float(input("Enter Cost of Appliance: "))
warranty_price = 0

# Calculations
if cost_of_appliance > 1000:
    warranty_price = (cost_of_appliance * .10)
else:
    warranty_price = (cost_of_appliance * .05)


# Display 
print("Name of Appliance: ", name_of_appliance)
print("Cost of Appliance: $", cost_of_appliance)
print("Warranty Price: $", warranty_price)
print("Total Cost (Including Warranty): ", (cost_of_appliance + warranty_price))
