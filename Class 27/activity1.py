# Step 1: Import ABC and abstractmethod from Python's abc module.
from abc import ABC, abstractmethod
# Step 2: Define an abstract base class Absclass that inherits from ABC.
class Absclass:
    def number(self,x):
        print(x)
    @abstractmethod
    def task(self):
        print("This is an abstract class!")
class child_class(Absclass):
    def task(self):
        print("We our inside child_class!")
test_obj = child_class()
test_obj.task()
test_obj.number(100)
# Step 3: Inside Absclass, define a normal method print(self, x) that prints the passed-in value.

# Step 4: Define an abstract method task(self) using the @abstractmethod decorator.

# Step 5: Define a subclass test_class that inherits from Absclass and implements task(self), printing its own message.

# Step 6: Create an object test_obj of test_class - this works because task() has been properly implemented.

# Step 7: Call test_obj.task() to run the overridden method, then call test_obj.print(100) to run the inherited normal method.