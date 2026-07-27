# 1) Ask the user to enter the numerator and store it in `numn`.
numerator=int(input("Enter a numerator:"))
# 2) Ask the user to enter the denominator and store it in `numd`.
denominator=int(input("Enter a denominator:"))
# 3) Check if `numn` is divisible by `numd`:
#    - Find the remainder when `numn` is divided by `numd`.
#    - If the remainder is 0, it means perfectly divisible.
if numerator%denominator==0:
    print("Number is divisble!")
else:
    print("Number is not divisble.")
# 4) If divisible, print that `numn` is divisible by `numd`.

# 5) Otherwise, print that `numn` is not divisible by `numd`.
