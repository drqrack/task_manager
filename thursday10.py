# Ask user to input their purchase amount as float
# If the purchase is 50 cedis or more, apply 10% discount and print amount to pay
# If the purchase is 100 cedis or more, apply 20% discount and print amount to pay
# If the purchase is less than 50 cedis, apply no discount and print amount to pay

purchase = float(input("Enter your amount: \n"))

# 20% Discount for more than GHc 100
discount_20 = float(0.2 * purchase)
newDiscount_20 = float(purchase - discount_20)

# 10% Discount for btw  Ghc 50 - Ghc 99
discount_10 = float(0.1 * purchase)
newDiscount_10 = float(purchase - discount_10)

if purchase >= 100:
    print(f"Your amount is : GhC {newDiscount_20}")

elif purchase >= 50 and purchase <= 99:
    print(f"Your amount is : GhC {newDiscount_10}")

elif purchase < 50:
    print(f"Your amount is : GhC {purchase}")