# hangman.py

import random

def hangman():
    # List of predefined words
    words = ["python", "java", "javascript", "php"]

    # Choose a random word from the list
    chosen_word = random.choice(words)

    # Display the initial state of the word
    guessed_word = "-" * len(chosen_word)

    # Number of attempts allowed
    attempts_left = 8

    # Letters that have already been guessed
    guessed_letters = set()

    while attempts_left > 0:
        print("\n" + guessed_word)
        print(f"Lives left: {attempts_left}")

        # Get the player's guess
        print(f"Input a letter: > ", end="")
        player_guess = input()

        # Check if the guessed letter is valid
        if len(player_guess) != 1 or not player_guess.islower():
            print("Please enter a lowercase English letter.")
            continue

        # Check if the guessed letter has already been guessed
        if player_guess in guessed_letters:
            print("You've already guessed this letter")
            continue

        # Add the guessed letter to the set of guessed letters
        guessed_letters.add(player_guess)

        # Check if the guessed letter is in the word
        if player_guess in chosen_word:
            if player_guess not in guessed_word:
                print("No improvements")
            else:
                print("You've already guessed this letter")
        else:
            print("That letter doesn't appear in the word")
            attempts_left -= 1

        # Update the guessed_word with the correctly guessed letter
        guessed_word = "".join([letter if letter == player_guess or guessed_word[idx] != '-' else '-' for idx, letter in enumerate(chosen_word)])

        # Check if the word has been completely guessed
        if '-' not in guessed_word:
            print(f"\n{guessed_word}\nYou guessed the word {chosen_word}!\nYou survived!")
            break

    # If the player runs out of attempts
    if attempts_left == 0:
        print("\nYou lost!")

if __name__ == "__main__":
    while True:
        print("HANGMAN")
        print('Type "play" to play the game, "exit" to quit: > ', end="")
        user_input = input().strip()

        if user_input == "play":
            hangman()
        elif user_input == "exit":
            print("See you later!")
            break
        else:
            print("Invalid input. Please enter either 'play' or 'exit'.")
