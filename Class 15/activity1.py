# Step 1: Define a function total_calc(bill_amount, tip_perc) with two positional parameters.
def total_calc(bill_amount, tip_perc):
    total=(bill_amount*tip_perc)/100
    Total=bill_amount + total
    return round(Total,2)
print(total_calc(150, 20))
# Step 2: Calculate the total by adding the tip percentage onto the bill amount.

# Step 3: Round the total to two decimal places using round().

# Step 4: Print the final total using an f-string.

# Step 5: Call total_calc(150, 20), passing the bill amount and tip percentage in that exact order.