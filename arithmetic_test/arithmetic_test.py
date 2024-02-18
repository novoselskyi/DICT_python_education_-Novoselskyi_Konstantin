import random

def get_level():
    """Запитує в користувача рівень складності."""
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        level = input("> ")

        if level == '1' or level == '2':
            return int(level)
        else:
            print("Incorrect format.")

def generate_task(level):
    """Генерує арифметичне завдання залежно від рівня складності."""
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operator = random.choice(['+', '-', '*'])
        task = f"{num1} {operator} {num2}"
        return task, eval(task)
    elif level == 2:
        num = random.randint(11, 29)
        task = str(num)
        return task, num ** 2

def get_user_answer():
    """Зчитує введення користувача та перевіряє правильність формату."""
    while True:
        user_answer = input("> ")

        try:
            user_answer = int(user_answer)
            return user_answer
        except ValueError:
            print("Incorrect format. Потрібно ввести ціле число.")

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(5):
        task, correct_answer = generate_task(level)
        print(task)

        user_answer = get_user_answer()

        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")

    save_result = input("> ").lower()
    if save_result in ['yes', 'y']:
        name = input("What is your name?\n> ")
        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} (simple operations with numbers 2-9).\n")
        print("The results are saved in 'results.txt'.")
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
