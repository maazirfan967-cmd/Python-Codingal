# Step 1: Define a function calculate_change(paid, price) that subtracts price from paid and returns the result.
def calculate_change(Paid,price):
    change = Paid - price
    return change
# Step 2: Set the snack price and print a greeting showing the price and the accepted coin values.
snack_price=12
print("Welcome to our vending machine!\nThe price for 1 snack is AED 12\nWe accept coins of 1 and notes of 5,10 and 20")
# Step 3: Start a while True loop that keeps asking for coins, using continue to reject any coin that isn't 1, 5, 10, or 25.
Total_inserted_coins=0
while True:
    coin=int(input("Enter a coin or note:"))
    if coin!=1 and coin!=5 and coin!=10 and coin!=20:
        print("INVALID Amount!")
        continue
    Total_inserted_coins+=coin
    print("Total inserted so far",Total_inserted_coins)
    if Total_inserted_coins>=snack_price:
        print("Enough money inserted.")
        break
change_due=calculate_change(Total_inserted_coins,snack_price)
if change_due==0:
    pass
else:
    print("Change given:",change_due)
print("Purchase Summary")
print("="*40)
print("Snack price:",snack_price)
print("Total inserted:",Total_inserted_coins)
print("Change:",change_due)
print("Thank you for shopping with us!")
print("="*40)
# Step 4: Add every valid coin to a running total and print how much has been inserted so far.

# Step 5: Use break to stop the loop the moment the total reaches or passes the snack price.

# Step 6: Call calculate_change() with the total inserted and the snack price to work out the change.

# Step 7: Use pass when the change is exactly zero, or print the change amount otherwise, then print a purchase summary.