class DailyMessage:
    def __init__(self):
        self.message = ""
    def get_message(self):
        self.message = input("Enter today's message:")
    def print_message(self):
        print(f"Message in uppercase:{self.message.upper()}")
daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()

class Helper_session:
    def __init__(self):
        print("Constructor created!")
    def __del__(self):
        print("Destructor called!")

def create_session():
    session = Helper_session()
    print("Helper session created!")
    return session
obj1 = create_session()

class PairFinder:
    def find_pair(self,numbers,target):
        look_up = {}
        for index, number in enumerate(numbers):
            needed_number = target - number
            if needed_number in look_up:
                return (look_up[needed_number], index)
            look_up[number] = index
        return None

numbers = (10,20,30,40,50,60,70,80,90)
target_value = int(input("Enter the target value:"))
result = PairFinder().find_pair(numbers, target_value)