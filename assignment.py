# Ask user to enter the cost price of a bike.
# If the cost price is greater than 100000, pay a 15% tax
# If the cost price is between 50000 and 100000, pay a 10% tax.
# If the cost price is less than or equal to 50000, pay a 5% tax.

cost_price = float(input("Enter the amount of the bike: \n"))

# 15% tax of cost price greater than 100000
tax_15 = (15/100) * cost_price

# 10% tax of cost price between 50000 and 100000
tax_10 = (10/100) * cost_price

# 5% tax of cost price less than 500000
tax_5 = (5/100) * cost_price

if cost_price > 100000:
    print(f"Amount to be paid: {tax_15}")

elif 50000 <= cost_price <= 100000:
    print(f"Amount to be paid: {tax_10}")

elif cost_price <= 50000:
    print(f"Amount to be paid: {tax_5}")