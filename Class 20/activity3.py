# Step 1: Create a tuple called weather holding seven values, one for each day of the week.
weather=(0,1,0,1,0,1,0)
# Step 2: Set two counters, sunny and rainy, both starting at zero.
sunny=0
rainy=0
# Step 3: Loop through all seven days using their index positions.
for i in range(7):
    if weather[i]==0:
        sunny+=1
    else:
        rainy+=1

if sunny<=rainy:
    print("Rainy Wins!")
else:
    print("Sunny Wins!")
# Step 4: Increase rainy by 1 whenever a day's value is 0, and increase sunny by 1 otherwise.

# Step 5: Compare the two final counts once the loop finishes.

# Step 6: Print "Good weather" if sunny is greater than rainy, and "Bad weather" otherwise.