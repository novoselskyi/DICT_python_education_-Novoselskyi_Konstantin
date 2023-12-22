# chatbot.py

import datetime

# Етап 1
bot_name = "DICT_Bot"
birth_year = datetime.datetime.now().year

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

# Етап 2
print("Please, remind me your name.")
your_name = input("> ")
print(f"What a great name you have, {your_name}!")

# Етап 3
print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3: "))
remainder5 = int(input("Enter remainder of dividing your age by 5: "))
remainder7 = int(input("Enter remainder of dividing your age by 7: "))

your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")

# Етап 4
print("Now I will prove to you that I can count to any number you want.")
count_to = int(input("> "))

for i in range(count_to + 1):
    print(f"{i} !")

print("Completed, have a nice day!")

# Етап 5
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

correct_answer = "2"

while True:
    user_answer = input("> ")
    if user_answer == correct_answer:
        break
    else:
        print("Please, try again.")

print("Congratulations, have a nice day!")

