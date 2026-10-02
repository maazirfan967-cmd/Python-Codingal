empty_list=[]
marks=[99,97,95,93,91]
print("Marks:",marks)

sample_list=[20,30,90]*2
print("Sample list:",sample_list)

print(len(marks))

print("First students's marks:",marks[0])
print("Last student's marks:",marks[-1])

firstthreemarks=marks[0:3]
print("First Three Marks:",firstthreemarks)

reversedmarks=marks[::-1]
print("Reversed Marks:",reversedmarks)

def match_marks(mark_list):
    matched_marks=[]
    count=0
    for i in mark_list:
        if mark_list[0]==mark_list[-1]:
            count+=1
            matched_marks.append(i)
    print("Marks which are matched:",matched_marks)
    return count
total=0
for i in marks:
    total+=i
print(f"Total marks are:{total}")

average=total/len(marks)
print(f"Average marks are:{average}")

marks.sort()
lowest_mark=marks[0]
highest_mark=marks[-1]
print(f"Lowest marks:{lowest_mark}")
print(f"Highest marks:{highest_mark}")