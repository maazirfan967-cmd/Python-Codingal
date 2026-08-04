print("===GROCERY COST COMPARISION TOOL===")
print("="*35)

Rice=25
Milk=21
Fruit=7
Baskets=3
Family_Members=4

Basket_Cost_Per_Person=(Rice + Milk + Fruit) * Baskets / Family_Members
print("Basket price per person are: ",Basket_Cost_Per_Person)

Total_Items=int(input("Enter the number of items:"))
People=int(input("Enter the number of family members:"))

if Total_Items % People==0:
    print("Total items are divisible by number of family members.")
else:
    print("Total number of people are not divisible by Total items.")

Recorded_Average=50
Incorrect_Weekly_Cost=20
Correct_Weekly_Cost=65
Total_Weeks=5

Recorded_Total= Recorded_Average * Total_Weeks
Corrected_Total= Recorded_Total - Incorrect_Weekly_Cost + Correct_Weekly_Cost

print("Corrected total:",Corrected_Total)

Corrected_Average= Corrected_Total / Total_Weeks
print("Corrected Average:",Corrected_Average)

Store_A_Average=40
Store_B_Average=50
Store_C_Average=45

print("Store a average:",Store_A_Average)
print("Store b average:",Store_B_Average)
print("Store c average:",Store_C_Average)

if Corrected_Average<Store_A_Average and Corrected_Average<Store_B_Average and Corrected_Average<Store_C_Average:
    print("Your corrected average is lower than all 3 stores.")
elif Corrected_Average>Store_A_Average and Corrected_Average>Store_B_Average and Corrected_Average>Store_C_Average:
    print("Your corrected average is higher than all three stores")
else:
    print("Your corrected total is in between of all 3 stores.")
print("="*54)