# Step 1: Create two fruit baskets as sets, each holding some repeated fruit names.
maaz={"Apple","Banana","Chery","Mango","Blueberry"}
irfan={"Apple","Mango","Avacado","Apple","Watermelon"}
# Step 2: Add a new fruit into the first basket using add().
maaz.add("Strawberry")
print(maaz)
print(irfan)
# Step 3: Find the fruits shared between both baskets using intersection().
common_items=maaz.intersection(irfan)
print(common_items)
# Step 4: Create an array of fruit counts using the array module.
import array as arr
a=arr.array("i",[1,1,2,3,4,5])
# Step 5: Add new fruit counts into the array using insert() and append().
print(a)
a.insert(3,7)
print(a)
a.append(7)
print(a)
# Step 6: Count how many times a chosen number appears in the array.
print(a.count(1))
# Step 7: Reverse the order of the fruit counts array and print the final organizer summary.
a.reverse()
print(a)