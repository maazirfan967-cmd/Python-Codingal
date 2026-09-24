# Step 1: Create student_data, a dictionary holding four students, each with their own nested details.
student_data={"S1":{"Name":"Abdullah","Age":11,"Grade":7},"S2":{"Name":"Maaz","Age":11,"Grade":6},"S3":{"Name":"Aahil","Age":12,"Grade":7},"S4":{"Name":"Abdullah","Age":11,"Grade":7}}
# Step 2: Create two empty containers - a result dictionary and a seen_keys list.
result_dictionary={}
seen_keys=[]
# Step 3: Loop through every student ID and its details inside student_data.
for i,j in student_data.items():
    unique=(j["Name"],j["Age"],j["Grade"])
    if unique not in seen_keys:
        seen_keys.append(unique)
        result_dictionary[i]=j
print(result_dictionary)
# Step 4: Build a unique_key from each student's name, class, and subjects.

# Step 5: Check whether that unique_key has already been seen before.

# Step 6: If it is new, remember it and keep that student in result; if not, skip it as a duplicate.

# # Step 7: Loop through result and print every unique student, one at a time.