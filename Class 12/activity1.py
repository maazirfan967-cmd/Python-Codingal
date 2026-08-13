# Step 1: Set up six counter variables (one per note value) plus counters for customers served and total dispensed, all starting at 0.
AED_100=0
AED_500=0
AED_1000=0
Customers_Served=0
Total_Dispensed=0
# Step 2: Start an outer while loop that keeps serving customers until the flag variable serving becomes False.
Serving=True
while Serving:
    Name=input("Enter your name:")
    withdrawal_amount=int(input("Enter the amout of money needed to be withdrawed:"))
    if withdrawal_amount<=0:
        print("Invalid amount!")
        continue
    print("Dispensing amount:",withdrawal_amount)
    Remaining=withdrawal_amount
    i=1
    while i<=3:
        if i==1:
            value=1000
        elif i==2:
            value=500
        elif i==3:
            value=100
        Count=Remaining // value
        print(f"Dispensing{Count}x{value}Unit notes={Count*value}")
        Remaining-=(Count*value)
        if value==1000:
            AED_1000+=Count
        elif value==500:
            AED_500+=Count
        elif value==100:
            AED_100+=Count
        i+=1
    Customers_Served+=1
    Total_Dispensed+=withdrawal_amount
    next_Customer=input("Next Customer?Yes/No").lower()
    if next_Customer!="yes":
        Serving=False



print("Total Customers served:",Customers_Served)
print("Total dispensed amount:",Total_Dispensed)


# Step 3: Ask for the customer's name and withdrawal amount; if the amount is invalid, print a message and continue back to the top of the loop.

# Step 4: Inside that same repeat, run an inner while loop that checks each of the six note values one at a time and works out how many of each note to dispense.

# Step 5: Update the matching counter variable for whichever note value was just dispensed, then ask if there is a next customer, setting serving to False if not.

# Step 6: Once the outer while loop ends, start an outer for loop stepping through each of the six note values to print the daily denomination report.

# Step 7: Inside that same repeat, run an inner for loop that prints one symbol for every note of that value dispensed across the whole.