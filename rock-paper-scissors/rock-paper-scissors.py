import random


def load_ratings():
    try:
        with open("rating.txt", "r") as file:
            ratings = {}
            for line in file:
                name, rating = line.strip().split()
                ratings[name] = int(rating)
            return ratings
    except FileNotFoundError:
        return {}


def save_ratings(ratings):
    with open("rating.txt", "w") as file:
        for name, rating in ratings.items():
            file.write(f"{name} {rating}\n")


def get_relations(options):
    relations = {}
    length = len(options)
    for idx, option in enumerate(options):
        weaker_than = options[(idx + 1):] + options[:(idx - length // 2)]
        stronger_than = options[(idx - length // 2):idx]
        relations[option] = {'weaker_than': weaker_than, 'stronger_than': stronger_than}
    return relations


def computer_choice(options):
    return random.choice(options)


def determine_winner(user_choice, computer_choice, relations):
    if user_choice == computer_choice:
        return "draw"
    elif computer_choice in relations[user_choice]['stronger_than']:
        return "win"
    else:
        return "lose"


def main():
    name = input("Enter your name: ").strip()
    print(f"Hello, {name}")

    ratings = load_ratings()
    user_rating = ratings.get(name, 0)

    options_input = input("Enter options separated by commas, or leave blank for default (rock,paper,scissors): ")
    options = options_input.split(',') if options_input else ['rock', 'paper', 'scissors']
    relations = get_relations(options)

    print("Okay, let's start")

    while True:
        user_input = input("Enter your choice, or type !exit to quit: ").lower()

        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {user_rating}")
        elif user_input in options:
            computer_choice_val = computer_choice(options)
            result = determine_winner(user_input, computer_choice_val, relations)

            if result == "draw":
                print(f"There is a draw ({user_input})")
                user_rating += 50
            elif result == "win":
                print(f"Well done. The computer chose {computer_choice_val} and failed")
                user_rating += 100
            else:
                print(f"Sorry, but the computer chose {computer_choice_val}")

            ratings[name] = user_rating
        else:
            print("Invalid input")

    save_ratings(ratings)


if __name__ == "__main__":
    main()
