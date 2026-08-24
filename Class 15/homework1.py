def total_bill(bill_amount,tip_perc):
    tip=(bill_amount*tip_perc)/100
    total=bill_amount+tip
    print("Please pay AED",total)
    return total

total_bill(150,20)

def seating_arrangements(guests):
    '''This function calculates the number of seating arrangements for guests.'''
    if guests==0 or guests==1:
        return 1
    else:
        return guests*seating_arrangements(guests-1)

print(seating_arrangements.__doc__)
print(seating_arrangements(1))
print(seating_arrangements(2))
print(seating_arrangements(3))
print(seating_arrangements(5))