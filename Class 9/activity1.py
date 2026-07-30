# Step 1:  Print the welcome banner: "=== Welcome to Ride Builder! ===".
print("===WELCOME TO RIDE BUILDER===")
# Step 2:  Print the Step 1 menu: "1 - Bike" and "2 - Car". Take input and store in choice.
print("Menu=1-Bike\n     2-Car")
Choice=input("What is your choice?(Car/Bike)")
# Step 3:  Write the outer if for choice == 1 (Bike branch).
if Choice=="Bike":
    print("In bike we have=\nMountain Bike\nE-Bike.")
    Type_OF_Bike=input("What type of bike would you like?")
    if Type_OF_Bike=="Mountain Bike":
        print("Good for mountain adventures:Can be used in any type of surfaces.")
    elif Type_OF_Bike=="E-Bike":
        print("Good for enviroment:Fast and smooth.")
    else:
        print("Invalid input:Check spelling.")
# Step 4:  Inside the Bike branch, print the Step 2 bike menu. Take input and store in bike_type.
elif Choice=="Car":
    print("In car we have=\nLamborghini\nFerrari")
    Type_OF_Car=input("What type of car would you like?")
    if Type_OF_Car=="Lamborghini":
        print("Luxirios and loud.")
    elif Type_OF_Car=="Ferrari":
        print("Fast and nice looks.")
    else:
        print("Invalid input:Check spelling.")
else:
    ("Invalid option:Type name of choice.")
print("=== Your custom ride is ready! ===")
# Step 5:  Write a nested if-else for bike_type: Scooty details if 1, Mountain Bike details if else.

# Step 6:  Write the outer elif for choice == 2 (Car branch).

# Step 7:  Inside the Car branch, print the Step 2 car menu. Take input and store in car_type.

# Step 8:  Write a nested if-else for car_type: Sedan details if 1, SUV details if else.

# Step 9:  Write the outer else to print an invalid choice message.

# Step 10:  Print the closing banner: "=== Your custom ride is ready! ===".

 


