habit_info = ("Playing Games",True,15,40)

weekly_habit = (1,0,0,1,0,1,1,1,0,1,0,0,1,0,1)

print(len(weekly_habit))

Day3 = weekly_habit[2]
print(f"Day 3:{Day3}")
Day7=weekly_habit[6]
print(f"Day 7:{Day7}")
First_Three_days = weekly_habit[0:3]
print(First_Three_days)

weekly_habit = weekly_habit + 1
print(f"After adding 1 more day:{weekly_habit}")

completed_days = weekly_habit.count(1)
missed = weekly_habit.count(0)

done=0
not_done=0
for i in range(0, len(weekly_habit)):
    if i==1:
        done+=1
    else:
        not_done+=1
print(f"Days completed:{done}")
print(f"Days not completed:{not_done}")