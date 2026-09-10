# Step 1: Create a list L holding several integers and print it as the original list.
L=[1,2,3,4,5,6,7,8]
print("Original list:",L)
# Step 2: Set a counter, count, to 0 to store the running sum.
count=0
# Step 3: Loop through every element in L and add it to count.
for i in L:
    count+=i
avg=count/len(L)
print("Sum:",count)
print("Average:",avg)
L.sort()
print(L[0])
print(L[-1])
# Step 4: Divide count by len(L) to calculate the average, storing it in avg.

# Step 5: Print the total sum and the average.

# Step 6: Sort L in ascending order using L.sort().

# Step 7: Print L[0] as the smallest element and L[-1] as the largest element.