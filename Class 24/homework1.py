class Pet:
    print("Hi,I'm inside the pet class!")
obj1 = Pet()
class PetProfile:
    category = "pet"
    def __init__(self,name,animal_type,age,favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food
pet1 = PetProfile("Simba","Cat",1.5,"Tuna")
pet2 = PetProfile("Ruby","Fish",0.1,"Fish Food")

print(f"Simba is a {pet1.category}")
print(f"Ruby is also a {pet2.category}")
print(f"{pet1.name} is a {pet1.animal_type},it is {pet1.age} years old, and its favourite food is {pet1.favourite_food}")
print(f"{pet2.name} is a {pet2.animal_type},it is {pet2.age} years old, and its favourite food is {pet2.favourite_food}")