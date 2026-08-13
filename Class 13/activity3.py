# Step 1: Take an integer input from the user and store it in rowSize.
rowSize=int(input("Enter an integer:"))
# Step 2: Use if/else on rowSize % 2 to decide halfDiamRow, the number of rows in the upper half.
if rowSize%2==0:
  Halfdiamrow=int(rowSize//2)
else:
  Halfdiamrow=int(rowSize//2)+1
# Step 3: Set space to halfDiamRow - 1, the starting number of leading spaces.
space=Halfdiamrow-1
# Step 4: For the upper half, loop i from 1 to halfDiamRow: print space blank spaces, decrease space by 1, then print 2*i - 1 increasing numbers.
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

# Step 5: After each upper row, call print() to move to the next line.

# Step 6: Reset space to 1 for the lower half.

# Step 7: For the lower half, loop i from 1 to halfDiamRow - 1: print space blank spaces, increase space by 1, then print numbers up to 2*(halfDiamRow - i) - 1.

# Step 8: After each lower row, call print() to move to the next line, completing the diamond.