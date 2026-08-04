print("===HOLIDAY ACTIVITY PLANNER===")
print("="*30)

print("We have 2 choices:\n1-Beach Holiday\n2-Mountain Holiday")
choice=int(input("Enter a choice(1 or 2):"))

if choice==1:
    print("You have choosen beach holiday!")
    print("At beach we have 2 activitys:\n1-Swimming\n2-Sandcastle Building")
    Beach_Choice=int(input("Enter a choice(1 or 2):"))
    if choice==1:
        print("Swimming:It is fun and also good for us.Have fun!")
    elif choice==2:
        print("Sandcastle Building:Fun and teamwork.Have fun!")
    else:
        print("Invalid Input:Enter number 1 or 2.")
elif choice==2:
    print("You have choosen moutain holiday!")
    print("At mountain we have 2 activitys\n1-Hiking\n2-Camping")
    Mountain_Choice=int(input("Enter a choice(1 or 2):"))
    if Mountain_Choice==1:
        print("Hiking:Pretty adventorous.Have fun!")
    elif Mountain_Choice==2:
        print("Camping:Remember to pack a tent.Have fun!")

print("="*27)
print("===HOLIDAY PLAN COMPLETE===")
print("="*27)