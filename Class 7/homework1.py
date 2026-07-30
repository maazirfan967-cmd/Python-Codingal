print("Welcome to my ASCII Value Checker!")
print("=" * 34)

char=input("Enter a single digit or letter:")
if type(char)==str and len(char)== 1:
    print("Valid input!Please wait while we proceed you to the next step.")
else:
    print("INVALID Input!Enter only 1 digit or letter.")
print("=" * 36)

if len(char)== 1:
    ascii_value=ord(char)
    print("Your character is:",char)
    print("Your character's ascii value is:",ascii_value)
else:
    print("")

if ascii_value>=65 and ascii_value<=90:
    print("Type:Uppercase Letter")
elif ascii_value >= 97 and ascii_value<=122:
    print("Type:Lowercase Letter")
elif ascii_value>=48 and ascii_value<=57:
    print("Type:Digit")
elif ascii_value==32:
    print("Type:Space")
else:
    print("Type:Special character")
    