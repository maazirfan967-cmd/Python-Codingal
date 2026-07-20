Temperature=int(input("What is the temperature?"))
if Temperature < 20:
    Outfit="Jacket"
    print("It is cold\nWear a",Outfit)
else:
    Outfit="T-Shirt"
    print("It is warm\nWear a",Outfit)
is_raining=input("Is it raining?")
if is_raining=="Yes":
    print("Bring an umbrella")
else:
    print("No need of umbrella")
Wind_Speed=int(input("What is the wind speed?"))
if Wind_Speed > 40:
    Windbreaker="yes"
    print("It is windy outside\nYou need a windbreaker",Windbreaker)
else:
    Windbreaker="No"
    print("It is calm today\nYou do not need a Windbreaker",Windbreaker)
Puddles=input("Are there any puddles on the road?")
if Puddles =="Yes":
    Shoes="Boots"
    print("There are puddles on the road\nWear",Shoes)
else:
    Shoes="Air Jordans"
    print("There are no puddles on the road\nWear",Shoes)
print("Weather Outfit picker--------------------------------")
print("Temperature",Temperature)
print("Outfit choosen",Outfit)
print("Raining",is_raining)
print("Wind breaker",Windbreaker)
print("Shoes choosen",Shoes)
print("-------------------------------------")