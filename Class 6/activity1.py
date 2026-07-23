print("====WEEk PLANNER====")
Day=input("What day is it?").strip().lower()
Weather=input("How is the weather?/Rainy/Cloudy/Windy/Sunny").strip().lower()
Homework=input("Did you complete your homework?").strip().lower()

print("Here is your plan for",Day)
if Day in ("saturday","sunday"):
    print("Its weekend:Have fun!")
elif Day=="Monday":
    print("It is the first day of the week.")
elif Day=="Friday":
    print("It is the last day of the week.")
elif Day in ("tuesday","wednesday","thursday"):
    print("Boring days:Get through them fast.")
else:
    print("Such days don't exist in our calender.")

if Weather=="rainy" or Weather=="cloudy":
    print("Carry an umbrella!")
elif Weather=="sunny" and Homework=="yes":
    print("Go call your friends!")

if not(Homework=="yes"):
    print("Complete your homework.")

if Weather=="rainy" and not Homework=="yes":
    print("It is rainy at the wrong time:You'll sadly have to be inside.")
elif Weather=="sunny" and Homework=="yes" and not(Day in("saturday","sunday")):
    print("Not the right day.")
elif Weather=="sunny" and Day in("saturday","sunday"):
    print("Finally you can go outside!!!")
else:
    print("Let's take 1 step at a time.")

print("==============================================================")

