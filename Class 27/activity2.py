# Step 1: Import ABC and abstractmethod from Python's abc module.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run.")
class snake(Animal):
    def move(self):
        print("I can crawl")
class dog(Animal):
    print("I can bark.")
class lion(Animal):
    print("I can roar.")
obj1 = Human()
obj1.move()
obj2 = snake()
obj2.move()
obj3 = dog()
obj3.move()
obj4 = lion()
obj4.move()
# Step 2: Define an abstract base class Animal that inherits from ABC.

# Step 3: Inside Animal, define an abstract method move(self) using pass as a placeholder.

# Step 4: Define a subclass Human that overrides move() to print "I can walk and run".

# Step 5: Define a subclass Snake that overrides move() to print "I can crawl".

# Step 6: Define a subclass Dog that overrides move() to print "I can bark".

# Step 7: Define a subclass Lion that overrides move() to print "I can roar".

# Step 8: Create one object of each subclass and call .move() on each - every object runs its own version of the method.