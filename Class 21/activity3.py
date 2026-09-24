# Step 1: Create country_code, a dictionary of three countries and their dialing codes.
country_code={"India":91,"UAE":971,"USA":1}
# Step 2: Print a label for the India lookup.
print(country_code.get("India","Not Found"))
# Step 3: Use .get() to look up India's code, with "Not Found" as a safe backup.

# Step 4: Print a label for the Japan lookup.
print(country_code.get("Japan","Not Found"))
# Step 5: Use .get() to look up Japan's code, which is missing, so the backup answer prints instead.