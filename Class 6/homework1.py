print("Welcome to my Library Visit Planner!")
print("For starting this planner,please answer the questions below.")

Day=input("What day is it?").strip().lower()
Weather=input("How is the weather?/Sunny/Windy/Rainy/Cloudy.").strip().lower()
Book_Return=input("Does a book need to be returned?")

if Day in ("saturday","sunday"):
    print("Weekend:Perfect time for a long library visit.")
elif Day=="friday":
    print("Last day of School:Return all your books.")
elif Day=="monday":
    print("First day of school:Use some of your time to check your reading list.")
elif Day in ("tuesday","wednesday","thursday"):
    print("Regular school day:Use some of your time to go to the library.")
else:
    print("PLEASE RECHECK WHAT YOU HAVE WRITTEN.")

if Weather=="sunny" and Book_Return=="yes":
    print("Perfect:Return book and choose a good book.")

if Weather=="rainy" or Weather=="cloudy":
    print("Better to avoid going to library but also ok with an umbrella.")

if not Book_Return=="yes":
    print("There is no book that needs to be returned.")

if Weather=="rainy" and Book_Return=="no":
    print("Stay at home and wait for the rain to stop.")
elif Weather=="sunny" and Day not in ("saturday","sunday"):
    print("Visit the Library for a short time.")
elif Day in ("saturday","sunday") and Book_Return=="yes":
    print("Perfect time for a long stay in the library.")
else:
    print("Check your schedule and plan a short library visit.")
print("")
print("======LIBRARY VISIT PLANNER COMPLETE!======")
