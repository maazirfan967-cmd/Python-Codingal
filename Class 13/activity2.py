# Step 1: Take an integer input from the user and store it in rows.
rows=int(input("Enter an integer:"))
# Step 2: Set number to 1, outside of both loops, so it can keep counting upward.
number=1
# Step 3: Print a heading message, "Floyd's Triangle".
print("Floyd's Triangle")
# Step 4: Start an outer loop with i running from 1 to rows, one pass per row.
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(number,end=" ")
    number+=1
  print()
# Step 5: Start an inner loop with j running from 1 to i, so row i prints i numbers.

# Step 6: Inside the inner loop, print number using end='  ', then increase number by 1.

# Step 7: After the inner loop finishes, call print() by itself to move to the next row.
