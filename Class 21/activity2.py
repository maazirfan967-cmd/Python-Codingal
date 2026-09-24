# Step 1: Create test_dict, a dictionary of five words, each holding a number value.
test_dict={"Apple":3,"Mango":15,"Blueberry":9,"Peach":7,"Orange":5}
# Step 2: Print the original dictionary before counting anything.
print(test_dict)
# Step 3: Store the target value K that you want to search for.
target_value=15
# Step 4: Set a counter, res, to zero before the loop begins.
res=0
# Step 5: Loop through every key in test_dict and compare its value to K.
for i in test_dict:
    if test_dict[i]==target_value:
        res+=1
print(res)
# Step 6: Add one to res every time a value matches K.

# Step 7: Print the final frequency count once the loop finishes.