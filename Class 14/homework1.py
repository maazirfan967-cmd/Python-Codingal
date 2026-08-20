def greet_customer():
    print("Welcome to my Art Supplies Shop!")
    print("Get your tools and start your own Creative Art.")

greet_customer()

price_per_item=float(input("Enter the price per item:"))
number_of_items=int(input("Enter the number of items:"))

def calculate_total(price,items):
    Total = price * items
    return Total
total2=calculate_total(price_per_item,number_of_items)
rounded_total=round(total2,2)
print("Total amount:",rounded_total)

paid_amount=float(input("Enter the amount paid:"))
def calculate_change(Paid,total):
    change = Paid - total
    return change
change_due=calculate_change(paid_amount,rounded_total)

def thank_you_message(items):
    if number_of_items<=5:
        print("Your art is going to be amazing!Please visit us again.😊")
    else:
        print("Thank you for visiting us!Plese come again.😊")

closing_message=thank_you_message(number_of_items)

print("Final Bill:")
print("Price:",price_per_item)
print("Items:",number_of_items)
print("Total cost:",rounded_total)
print("Amount paid:",paid_amount)
print("Change:",change_due)
print(closing_message)