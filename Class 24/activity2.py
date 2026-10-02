# Step 1: Define a class named Employee.
class Employee:
  def __init__(self):
    print("Employee created!")
  def __del__(self):
    print("Destructor called!")
def Create_obj():
  print("Making Object")
  employee_obj=Employee()
  return employee_obj
abc=Create_obj()
print(abc)
# Step 2: Inside the class, define __init__(self) as the constructor, printing "Employee created" when it runs.

# Step 3: Define __del__(self) as the destructor, printing "Destructor called" when it runs.

# Step 4: Define a function Create_obj() that prints "Making Object...", creates an Employee object, prints "function end...", then returns that object.

# Step 5: Print "Calling Create_obj() function..." before calling the function.

# Step 6: Call Create_obj() and store the returned object in obj.

# Step 7: Print "Program End..." - Python automatically calls the destructor once the program finishes and the object is no longer needed.