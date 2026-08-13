print("===HOMEWORK COMPLETION CHECKER===")
print("=" * 33)
total_homework= 4
original_count=total_homework

completed_count= 0
Task_num= 1

while Task_num<=total_homework:
    if Task_num==1:
        Next_Homework="Science Project"
    elif Task_num==2:
        Next_Homework="English Essay"
    elif Task_num==3:
        Next_Homework="Maths Textbook Pages"
    elif Task_num==4:
        Next_Homework="SST Lap Book"
    else:
        Next_Homework="Good Job"
    Answer=input(f"Is task 1 completed?(Yes/No){Next_Homework}").lower()
    if Answer=="yes":
        Task_num+=1
        completed_count+=1
        total_homework-=1
        print("Good Job!")
    else:
        print("Okay, complete it and check again.")
    print("Homework remaining:",total_homework)

Test_Value=0
Safety_Counter=0
while Test_Value==0:
    Safety_Counter+=1
    if Safety_Counter==3:
        break

print("===HOMEWORK CHECK COMPLETE===")
print("Total Tasks:",total_homework)
print("Completed tasks:",completed_count)
print("Tasks Remaining:",total_homework-completed_count)
print("==============================")