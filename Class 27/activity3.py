# Step 1: Define a class India with three methods: capital(), language(), and type(), each printing a fact about India.
class India:
    def capital(self):
        print("Dehli")
    def language(self):
        print("Hindi")
class USA:
    def capital(self):
        print("Washington D.C")
    def language(self):
        print("English")
obj_ind = India()
obj_usa = USA()
for i in (obj_ind,obj_usa):
    i.capital()
    i.language()
# Step 2: Define a class USA with the exact same three method names, each printing a fact about the USA.

# Step 3: Create one object of each class: obj_ind and obj_usa.

# Step 4: Use a for loop to iterate through (obj_ind, obj_usa).

# Step 5: Inside the loop, call country.capital(), country.language(), and country.type() on each object - Python automatically runs each class's own version, with no inheritance needed.