print("===STAR PYRAMID===")
rows=int(input("Enter an integer for number of rows:"))

for i in range(rows):
    for j in range(i+1):
        print("😊",end=" ")
    print()

rows=int(input("Enter an integer again for the number of rows in your floyd's triangle:"))
number=1

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(number,end=" ")
        number+=1
    print()

rowSize=int(input("Enter an integer:"))
if rowSize%2==0:
  Halfdiamrow=int(rowSize//2)
else:
  Halfdiamrow=int(rowSize//2)+1
space=Halfdiamrow-1
for i in range(1,Halfdiamrow+1):
  for j in range(1,space+1):
    print(end=" ")
  space-=1
  number=1
  for j in range(i*2-1):
    print(number,end=" ")
    number+=1
  print()

space=1
for i in range(1,Halfdiamrow):
  for j in range(1,space+1):
    print(end=" ")
  space+=1
  number=1
  for j in range(1,2*(Halfdiamrow-i)):
    print(number,end=" ")
    number+=1
  print()

