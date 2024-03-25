import random

def initialize_game():
    full_set = [[i, j] for i in range(7) for j in range(i, 7)]
    random.shuffle(full_set)
    player_pieces = [list(piece) for piece in full_set[:7]]
    computer_pieces = [list(piece) for piece in full_set[7:14]]
    stock_pieces = [list(piece) for piece in full_set[14:]]

    domino_snake = []
    status = ""
    max_double = max([max(piece) for piece in stock_pieces if piece[0] == piece[1]], default=None)
    if max_double is not None:
        domino_snake.append([max_double, max_double])
        status = "computer"
    else:
        random.shuffle(stock_pieces)
        status = "player"

    return stock_pieces, computer_pieces, player_pieces, domino_snake, status


def print_snake(domino_snake):
    if len(domino_snake) > 6:
        print(*domino_snake[:3], sep=",", end=", ..., ")
        print(*domino_snake[-3:], sep=",")
    else:
        print(*domino_snake, sep=",")

def print_game_interface(stock_size, computer_pieces, player_pieces, domino_snake, status):
    print("=" * 70)
    print("=" * 13 + " Game Interface " + "=" * 13)
    print("Stock size:", stock_size)
    print("Computer pieces:", len(computer_pieces))
    print_snake(domino_snake)
    print("Your pieces:")
    for i, piece in enumerate(player_pieces, 1):
        print(f"{i}: {piece}")
    if status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    elif status == "player":
        print("Status: It's your turn to make a move. Enter your command.")

def is_valid_move(piece, side, domino_snake):
    if side == "left":
        if piece[0] == domino_snake[0][0] or piece[1] == domino_snake[0][0]:
            return True
    elif side == "right":
        if piece[0] == domino_snake[-1][1] or piece[1] == domino_snake[-1][1]:
            return True
    return False

def player_move(player_pieces, domino_snake, stock_pieces):
    while True:
        try:
            move = input("> ")
            if move == "0":
                if len(stock_pieces) > 0:
                    piece = stock_pieces.pop(random.randint(0, len(stock_pieces) - 1))
                    return piece, "skip"
                else:
                    print("No pieces left in the stock.")
            else:
                side, num = map(int, move.split(":"))
                if abs(num) > len(player_pieces):
                    raise ValueError
                piece = player_pieces.pop(num - 1)
                if is_valid_move(piece, side, domino_snake):
                    if side > 0:
                        return piece, "right"
                    else:
                        return piece, "left"
                else:
                    print("Illegal move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def computer_move(computer_pieces, domino_snake, stock_pieces):
    while True:
        piece = list(computer_pieces.pop(random.randint(0, len(computer_pieces) - 1)))
        side = random.choice(["left", "right", "skip"])
        if side == "skip":
            return piece, "skip"
        elif is_valid_move(piece, side, domino_snake):
            return piece, side


def apply_move(piece, side, domino_snake):
    if side == "left":
        if piece[0] == domino_snake[0][0]:
            domino_snake.insert(0, piece)
        else:
            piece.reverse()
            domino_snake.insert(0, piece)
    elif side == "right":
        if piece[1] == domino_snake[-1][1]:
            domino_snake.append(piece)
        else:
            piece.reverse()
            domino_snake.append(piece)

def game_over(domino_snake, stock_pieces, player_pieces, computer_pieces):
    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        return True
    elif len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        return True
    elif len(stock_pieces) == 0:
        snake_ends = [domino_snake[0][0], domino_snake[-1][1]]
        if snake_ends.count(snake_ends[0]) == 8:
            print("Status: The game is over. It's a draw!")
            return True
    return False

def assign_scores(computer_pieces, domino_snake):
    scores = {}
    # Підрахунок кількості випадань кожної цифри в наявних кісточках та змійці
    counts = [0] * 7
    for piece in computer_pieces + sum(domino_snake, []):
        if isinstance(piece, list):
            counts[piece[0]] += 1
            counts[piece[1]] += 1
    # Присвоєння оцінок кісточкам
    for piece in computer_pieces:
        score = sum(piece)
        for num in piece:
            score += counts[num]
        scores[tuple(piece)] = score
    return scores


def main():
    stock_pieces, computer_pieces, player_pieces, domino_snake, status = initialize_game()

    while True:
        print_game_interface(len(stock_pieces), computer_pieces, player_pieces, domino_snake, status)

        if status == "player":
            piece, side = player_move(player_pieces, domino_snake, stock_pieces)
        elif status == "computer":
            piece, side = computer_move(computer_pieces, domino_snake, stock_pieces)

        if side != "skip":
            apply_move(piece, side, domino_snake)

        if game_over(domino_snake, stock_pieces, player_pieces, computer_pieces):
            break

        status = "player" if status == "computer" else "computer"

if __name__ == "__main__":
    main()
