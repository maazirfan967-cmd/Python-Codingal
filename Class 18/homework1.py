import random
import math

lucky_number=random.randint(1,10)
print(f"Your lucky number is {lucky_number}!")

fun_activities="Football","Basketball","Hide and Seek"
print("Your random fun activity is:",random.choice(fun_activities))

secret_num=random.randint(1,5)
while True:
    guess=int(input("Enter a random number between 1 and 5(Note:1 and 5 are also included.):"))
    if guess==secret_num:
        print("Correct guess!You won.")
        break
    else:
        print("Wrong guess!Try again.")

number=float(input("Enter any decimal number:"))
print("Its ceiling value is:",math.ceil(number))
print("Its floor value is:",math.floor(number))

x=10
y=-15
print("Copysign:",math.copysign(x,y))
num2=-20
print("Absolute value of -20:",math.fabs(num2))

num1=int(input("Enter an integer:"))
num2=int(input("Enter another integer:"))
print("The gcd of these two numbers are:",math.gcd(num1,num2))