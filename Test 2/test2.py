def add(a,b):
    result=a+b
    return result

def subtract(a,b):
    result=a-b
    return result

def multiply(a,b):
    result=a*b
    return result

def divide(a,b):
    result=a/b
    return result

try:
    a=float(input("Enter a number:"))
    b=float(input("Enter a number again for addition:"))
    print(add(a,b))
except ValueError:
    print("Please enter a valid input!")
try:
    a1=float(input("Enter a number for subtraction:"))
    b1=float(input("Enter a number again:"))
    print(subtract(a1,b1))
except ValueError:
    print("Please enter a valid input!")
try:
    a2=float(input("Enter a number for multiplication:"))
    b2=float(input("Enter a number again:"))
    print(multiply(a2,b2))
except ValueError:
    print("Please enter a valid number!")
try:
    a3=float(input("Enter a number for division:"))
    b3=float(input("Enter a number again:"))
    print(divide(a3,b3))
except ZeroDivisionError:
    print("No number can be divided by Zero!")
except ValueError:
    print("Please enter a valid number!")
