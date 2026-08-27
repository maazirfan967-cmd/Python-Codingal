# Step 1: Import the random module.
import random
# Step 2: Start a while True loop so the game can repeat for multiple rounds.
while True:
    choice=input("Enter your choice(Rock,Paper,Scissors):")
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        comp_choice="Rock"
    elif computer_choice==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"
    print(f"Computer choice:{comp_choice}")
    if choice==comp_choice:
        print("It's a tie!")
    elif choice=="Rock" and comp_choice=="Paper":
        print("The computer won!")
    elif choice=="Rock" and comp_choice=="Scissors":
        print("You won!")
    elif choice=="Paper" and comp_choice=="Scissors":
        print("The computer won!")
    elif choice=="Paper" and comp_choice=="Rock":
        print("You won!")
    elif choice=="Scissors" and comp_choice=="Paper":
        print("You won!")
    elif choice=="Scissors" and comp_choice=="Rock":
        print("The computer won!")
    again=input("Do you want to play again?(Yes/No)").lower()
    if again!="yes":
        break
# Step 3: Ask the player for their choice - rock, paper, or scissors.

# Step 4: Generate a random number from 1 to 3 using random.randint(1, 3).

# Step 5: Use if/elif to turn that number into the computer's move: 1 becomes rock, 2 becomes paper, and anything else becomes scissors.

# Step 6: Print both the player's and computer's choices using an f-string.

# Step 7: Compare the two choices with if/elif to decide whether it's a tie, a win, or a loss, printing the result.

# Step 8: Ask if the player wants to play again, and break out of the loop if the answer isn't "y".