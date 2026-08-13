print("===NUMBER GUESSING GAME===")
Heart=5
working=True
while working:
    secret=15
    User_number=int(input("Enter a number between 0 and 50:"))
    if User_number==15:
        print("You Won!Nice guessing.")
        break
    else:
        print("Please enter again.")
        Heart-=1

    if Heart==0:
        print("You ran out of Hearts.Good Luck next time")
        break
    else:
        print("You still have",Heart,"Hearts.")
    

