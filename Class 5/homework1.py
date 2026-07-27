Temperature=int(input("What is the temperature today?"))
if Temperature < 20:
    Activity="Play outside."
    print("It is a cool day.Go",Activity)
else:
    Activity="Indoor reading."
    print("It is a warm day.Go",Activity)

Rain=input("Is it raining outside?")
if Rain=="yes":
    print("Bring an umbrella!")

Homework_Time=int(input("How much time will your homework take?"))
if Homework_Time > 40:
    Study_Break="Yes"
    print("It is a long homework.Take a short break before you start.")
else:
    Study_Break="No"
    print("It is a short homework.No need of break.")

Free_Time=input("Do you have free time?")
if Free_Time =="yes":
    Task="Hobby time"
    print("You have free time today.Use your time for your hobby.")
else:
    Task="Planning Time"
    print("You dont have much free time.Use a little of your time for planning time.")

print("====DAILY ACTVITY PLANNER====")
print("Temperature:",Temperature)
print("Activity choosen:",Activity)
print("Raining:",Rain)
print("Study break:",Study_Break)
print("Final Task:",Task)
print("=============================")