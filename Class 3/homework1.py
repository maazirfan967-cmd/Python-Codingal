print("Welcome to my student badge program!")
Name=input("What is your name?")
School_Club=input("Which school club are you in?")

Member_Number=737
Points_Earned=4.5
Event_Count=3
Meeting_Hours=100
Active_Status="True"

print("Name",type(Name))
print("School Club",type(School_Club))
print("Member Number",type(Member_Number))
print("Points earned",type(Points_Earned))
print("Event count",type(Event_Count))
print("Meeting hours",type(Meeting_Hours))
print("Active status",type(Active_Status))

Member_number_str=str(Member_Number)
Event_Count_str=str(Event_Count)
Points_str=str(Points_Earned)
Active_Status_str=str(Active_Status)

First=Name[0:3]
Last=Name[-1:]
print(First+Last)

Reversed=School_Club[::-1]
print(Reversed)

