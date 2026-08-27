valid=False
while not valid:
    try:
        bill_amount, discount_perc, people=input("Enter the bill amount,discount percentage, and the people: ").split(",")
        bill_amount=float(bill_amount)
        discount_perc=float(discount_perc)
        people=int(people)
        if bill_amount<=0 or discount_perc<=0 or people<=0:
            raise ValueError
        discount_amount=(bill_amount-discount_perc)/100
        final=(bill_amount-discount_amount)
        amount_per_person=final/people
    except ValueError:
        print("Please enter a positive number!")
    except ZeroDivisionError:
        print("No number can be divided by 0!")
    else:
        print("Original amount:",bill_amount)
        print("Discount percentage:",discount_perc)
        print("Discount amount:",discount_amount)
        print("Final amount:",final)
        print("Amount per person:",round(amount_per_person,0))
        valid=True
    finally:
        print("Discounted!!!")