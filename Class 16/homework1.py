def calculate_change(paid,total):
    change=paid-total
    return change
ticket_price=30
total_inserted=0
coins_inserted=0
while True:
    print("Total needed to be paid:",ticket_price)
    coin=int(input("Enter a coin:"))
    if coin!=1 and coin!=5 and coin!=10:
        print("INVALID Coin!!!")
        continue
    else:
        total_inserted+=coin
        coins_inserted+=1
        print("Total inserted:",total_inserted)
    if total_inserted>=ticket_price:
        print("Enough money inserted!")
        break
change_due=calculate_change(total_inserted,ticket_price)
if change_due==0:
    pass
else:
    print("Here is your change:",calculate_change)
print("Ticket price:",ticket_price)
print("Total insereted:",total_inserted)
print("Change given:",change_due)
print("Thank you for paying.\nHere's your ticket...")