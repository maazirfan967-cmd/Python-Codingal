# Step 1: Define a function match_words(words) that takes a list of words.
def match_words(words):
    list1=[]
    ctr=0
    empty_list=[]
    for i in words:
        if i[0]==i[-1]:
            ctr+=1
            list1.append(i)
    print(list1)
    return ctr
abc=match_words(['Maaz','Huzaifa','Sabiha','Irfa','abdulla'])
print(abc)
# Step 2: Set a counter ctr to 0 and an empty list lst to store matching words.

# Step 3: Loop through every word in the words list.

# Step 4: Check whether the word's length is greater than 1 and its first character equals its last character.

# Step 5: If true, add 1 to ctr and append the word to lst.

# Step 6: Print the list of matching words once the loop finishes.

# Step 7: Return ctr, call match_words() with a sample list, and print the final count.