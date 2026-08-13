print("===GROCERY BILLING QUEUE===")
print("="*27)
Low_price= 0
Medium_price= 0
High_price= 0
Total_Sales= 0
Customers_Served= 0

Billing= True
while Billing:
    Customer_Name=input("Please enter your name:")
    Total_Items=int(input("Enter total items:"))
    if Total_Items<=0:
        print("Invalid Input!Please try again.")
        continue

    item_number=1
    while item_number<Total_Items:
        item_name=input("Enter item name:")
        price=int(input("Enter item price:"))
        quantity=int(input("Enter quantity of item:"))
        if price<=0 or quantity<=0:
            print("Invalid Price or Quantity.Please enter again.")
            continue
        item_total= price*quantity
        customer_bill=0
        customer_bill+=item_total

        if price<=10:
            Low_price+=quantity
        elif price<=25:
            Medium_price+=quantity
        else:
            High_price+=quantity
        Total_Sales+=customer_bill
        Customers_Served+=1

for slot in range(1, 4):                    
    if slot == 1:
        print("Low priced items:",Low_price)
    elif slot == 2:
        print("Medium priced items:",Medium_price)
    else:
        print("High priced items:",High_price)


        
    