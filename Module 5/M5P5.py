# Christopher Monarrez M5P5

# Variables
users_lase_name = str(input("Enter Your Last Namme: "))
numnber_of_dependents = int(input("Enter Number of Dependents: "))
gross_income = float(input("Enter Your Gross Income: $"))
adjusted_gross_income = (gross_income - (numnber_of_dependents * 12000))
tax_rate = 0


# Calculations
if adjusted_gross_income > 50000:
    tax_rate = .2
else:
    tax_rate = .1

# Income Tax Var. and $0 if statement
income_tax = adjusted_gross_income * tax_rate

if income_tax < 0:
    income_tax = 100



# Display
print()
print()
print("Last Name: ", users_lase_name)
print("Gross Income: ", gross_income)
print("Number of Dependents: ", numnber_of_dependents)
print("Adjusted Gross Income: ", adjusted_gross_income)
print("Income Tax: ", income_tax)
