# Step 1: Define a function factorial(x) with a docstring describing what it calculates.
def factorial(x):
    '''This_function_is_to_find_a_factorial_of_a_number'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(5))
print(factorial(10))
# Step 2: Write the base case: if x is 0 or 1, return 1 directly.

# Step 3: Write the recursive case: otherwise, return x multiplied by factorial(x-1).

# Step 4: Print factorial.__doc__ to display the function's docstring.

# Step 5: Call factorial() on 0, 1, 2, 5, and 10, printing each result.