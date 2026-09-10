# Step 1: Create a tuple called tuplex holding four different data types together.
tuplex=('Maaz',7,3.7,True)
# Step 2: Create a new tuple called tuplex holding six integers.
tuplex=(1,2,3,4,5,6)
print("Tuple 1:",tuplex)
# Step 3: Use the + operator to add a single new item, 9, onto tuplex, since tuples cannot be changed directly.
add=tuplex + (9,)
print("Added Tuple:",add)
# Step 4: Create tuple1 and use .count(50) to count how many times 50 appears inside it.
tuplex.count(5)
# Step 5: Create a longer tuple called tuplex to practice slicing.
tuplex2=(tuplex[3:5])
print("Sliced Tuple:",tuplex2)
# Step 6: Slice tuplex[3:5] to get a range starting from index 3.
tuplex=(tuplex[:5])
print("Tuplex:",tuplex)
# Step 7: Slice tuplex[:6] to get every item from the very beginning through index 5.