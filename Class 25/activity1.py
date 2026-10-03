# Step 1: Create a parent class called FamilyMember that stores shared traits like eye colour and height.
class FamilyMember():
    def __init__(self,eye_color,height):
        self.eye_color=eye_color
        self.height=height
    def show_traits(self):
        print(self.eye_color)
        print(self.height)
# Step 2: Create a child class called Kid that inherits from FamilyMember.
class Kid(FamilyMember):
    def __init__(self,name,age,eye_color,height):
        self.name=name
        self.age=age
        super().__init__(eye_color,height)
    def show_traits(self):
        print(self.name)
        print(self.age)
        super().show_traits()
    def Hobby(self,hobby):
        print("My hobby is:",hobby)
obj=Kid("Maaz",11,"brown",157)
obj.show_traits()
obj.Hobby("Football")
print(issubclass(Kid,FamilyMember))
# Step 3: Give Kid its own details, then use super().__init__() to pull in the parent's traits too.

# Step 4: Override show_traits() inside Kid to display the kid's own details plus the inherited ones.

# Step 5: Add a brand new method inside Kid that only the child class has.

# Step 6: Create a Kid object and call both the overridden method and the new method.

# Step 7: Check with issubclass() whether Kid truly is a subclass of FamilyMember.