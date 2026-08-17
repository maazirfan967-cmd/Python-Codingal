# Step 1: Define and call greet_customer() to welcome every customer to the stand.
def greet_customer():
    print("Welcome to my Lemonade stand!")
# Step 2: Ask for the price per cup and the number of cups sold.
price_per_cup=float(input("Enter the price per cup:"))
Cups_sold=float(input("Enter the amount of cups:"))
# Step 3: Define and call calculate_total() to return the total cost using arguments.
def calculate_total(price, cup):
    Total= price * cup
    return round(Total,0)
# Step 4: Round the total using the built-in round() function and print it.

# Step 5: Define and call calculate_change() to return the change due.
def calculate_change(paid, total):
    change= paid - total
    return change

# Step 6: Define and call thank_you_message() to return a personalized closing line.
def thank_you_message():
    print("Thank you for shopping with us.Please visit us again.")
# Step 7: Print the final lemonade stand receipt with every calculated value.
greet_customer()
Total2=calculate_total(price_per_cup, Cups_sold)
print("Total amount",Total2)
paid_amount=float(input("Enter the amount needed to be paid:"))
Change2=calculate_change(paid_amount, Total2)
print("Change Given:",Change2)
thank_you_message()

