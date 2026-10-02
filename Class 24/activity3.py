# Step 1: Define a class named pair_elements.
class pair_elements:
  def twosum(self,nums,target):
    dictionary1={}
    for i,num in enumerate(nums):
      if target-num in dictionary1:
        return (dictionary1[target-num],i)
      dictionary1[num]=i
abc=int(input("Enter the sum which you'd like to search:"))
obj1=pair_elements()
print(obj1.twosum((10,20,30,40,50,60),abc))
# Step 2: Inside the class, define a method twoSum(self, nums, target).

# Step 3: Inside the method, create an empty dictionary lookup to remember numbers you've already seen and their positions.

# Step 4: Loop through nums using enumerate(nums), so you get each position i and value num together.

# Step 5: On each pass, check whether target - num is already a key in lookup - if it is, return a tuple of that stored position and the current position i.

# Step 6: If not found yet, store the current number and its position in lookup using lookup[num] = i.

# Step 7: Take the target sum as input from the user, call twoSum() on the tuple (10, 20, 30, 40, 50, 60, 70), and print the two positions using an f-string.