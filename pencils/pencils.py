import random

def main():
    # Запитуємо користувача про кількість олівців
    while True:
        try:
            num_pencils = int(input("How many pencils would you like to use:\n"))
            if num_pencils <= 0:
                print("The number of pencils should be positive")
            else:
                break
        except ValueError:
            print("The number of pencils should be numeric")

    # Запитуємо користувача про ім'я першого гравця
    while True:
        first_player = input("Who will be the first (John, Jack):\n")
        if first_player not in ["John", "Jack"]:
            print("Choose between 'John' and 'Jack'")
        else:
            break

    # Створюємо рядок символів "|" для відображення кількості олівців
    pencils_str = "|" * num_pencils

    # Виводимо рядок символів та ім'я першого гравця
    print(pencils_str)
    print(f"{first_player}'s turn!")

    # Головний цикл гри
    while num_pencils > 0:
        if first_player == "Jack":
            # Якщо Jack перший, він виконує хід відповідно до стратегії
            pencils_to_take = num_pencils % 4
            if pencils_to_take == 0:
                pencils_to_take = random.randint(1, 3)
            print(f"Jack's turn: {pencils_to_take}")
            num_pencils -= pencils_to_take
            pencils_str = "|" * num_pencils
            print(pencils_str)
            if num_pencils == 0:
                break
            first_player = "John"
        else:
            # Користувач вибирає кількість олівців
            while True:
                try:
                    remove_pencils = int(input("> "))
                    if remove_pencils < 1 or remove_pencils > 3:
                        print("Possible values: '1', '2' or '3'")
                    elif remove_pencils > num_pencils:
                        print("Too many pencils were taken")
                    else:
                        break
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
            # Видаляємо олівці з загальної кількості
            num_pencils -= remove_pencils

            # Виводимо стан гри
            pencils_str = "|" * num_pencils
            print(pencils_str)

            # Перевіряємо, чи ще залишилися олівці
            if num_pencils == 0:
                break

            # Визначаємо наступного гравця
            first_player = "Jack"

    # Визначаємо переможця
    winner = "Jack" if first_player == "John" else "John"
    print(f"{winner} won!")

if __name__ == "__main__":
    main()
