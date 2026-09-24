student={"Maaz":99,"Huzaifa":95,"Sabiha":100,"Irfan":97,"Samarth":96}

counter=0
for values in student.values():
    counter+=values
avg=counter/5
print(avg)

storeValues=student.values()
print(storeValues)
min1=min(storeValues)
max1=max(storeValues)
for i in student:
    if student[i]==min1:
        print("Lowest:",i)
    if student[i]==max1:
        print("Highest:",i)

name=input("Enter the student name:")
choosen=student.get(name,"Student not found!")
print(choosen)


