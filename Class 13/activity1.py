# Step 1: Print a heading message describing the pattern.
print("Shape maker")
# Step 2: Take an integer input from the user and store it in n, the number of rows.
n=int(input("Enter a integer:"))
# Step 3: Start an outer loop with i running from 0 to n - 1, one pass per row.
for i in range(n+1):
    for j in range(n+1):
        print("😂",end="")
    print()
# Step 4: Start an inner loop with j running from 0 to i, so row i prints i + 1 stars.

# Step 5: Inside the inner loop, print "* " using end="" so every star stays on the same line.

# Step 6: After the inner loop finishes, call print() by itself to move to the next row.

# Step 7: Repeat until the outer loop has printed all n rows, forming a growing half-pyramid.