# Step 1: Start a try block.
try:
    n1=int(input("Enter integer 1:"))
    n2=int(input("Enter integer 2:"))
    divide=n1/n2
except ZeroDivisionError:
    print("Division by 0 is an error!!!")
except ValueError:
    print("Only Valid Whole Numbers!!!")
except:
    print("Invalid Input!!!")
else:
    print("No Exceptions!")
finally:
    print("This will execute no matter what!")
# Step 2: Ask the user for a first number and a second number, converting each with int(input(...)).

# Step 3: Divide the first number by the second and print the result.

# Step 4: Add an except ZeroDivisionError block, printing "Division by zero is error !!" if the second number is 0.

# Step 5: Add an except ValueError block, printing a message asking for valid whole numbers if either entry isn't a number.

# Step 6: Add a plain except block, printing "Wrong input" for any other unexpected error.

# Step 7: Add an else block that prints "No exceptions" only if the division succeeded with no errors at all.

# Step 8: Add a finally block that prints "This will execute no matter what", always running regardless of the outcome.