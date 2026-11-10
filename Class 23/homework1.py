books = ["Running Wild","Cosmic","Global"]
copy_counts = [10,5,0]
library = {book:count for book,count in zip(books, copy_counts)}
print(f"Full Library Stock:{library}")
available_books = [book for book in books if library[book] > 0]
print(f"Books Available:{available_books}")
Choice = input("Which book would you like?")
if Choice not in library or library[Choice] == 0:
    print(f"{Choice}is not available!")
    exit()
late_fees = [10,8,6,4,2]
extra_fee = int(input("Enter the extra library fee to add to every book:"))
updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))
print("Updated Late Fees:", updated_fees)
book_index = books.index(Choice)
chosen_fee = updated_fees[book_index]
print(f"Late fee for:{Choice} after update:{chosen_fee}")
library[Choice] = library[Choice] - 1
print(Choice, "borrowed! Remaining copies:", library[Choice])
print("")
print("===== LIBRARY BOOK AVAILABILITY CHECKER =====")
print("Book Borrowed:", Choice)
print("Late Fee:", chosen_fee)
print("Updated Library Stock:", library)
print("=============================================")