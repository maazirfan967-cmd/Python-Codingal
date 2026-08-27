# Step 1: Import the random module.
import random
# Step 2: Set a variable playing to True to control the game loop.
playing=True
# Step 3: Generate a secret number between 0 and 9 using random.randint(0, 9), converting it to a string.
number=str(random.randint(0,9))
# Step 4: Print instructions explaining the guessing game to the player.
print("Choose a number between 0 and 9!")
# Step 5: Start a while playing loop that keeps asking for a guess.
while playing:
    ans=(input("Enter a number:"))
    if ans==number:
        print("You won!")
        break
    else:
        print("You lose!")
        
# Step 6: If the guess matches the secret number, print a winning message showing the number, then break out of the loop.

# Step 7: Otherwise, print a message asking the player to try again, and the loop continues.