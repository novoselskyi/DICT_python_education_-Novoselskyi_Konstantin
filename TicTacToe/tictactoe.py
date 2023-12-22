def print_board(board):
    print("---------")
    for row in board:
        print("|", " ".join(row), "|")
    print("---------")

def analyze_board(board):
    x_wins = check_winner(board, 'X')
    o_wins = check_winner(board, 'O')
    empty_cells = any('_' in row for row in board)

    if x_wins and o_wins:
        return "Impossible"
    elif x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif empty_cells:
        return "Game not finished"
    else:
        return "Draw"

def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]) or all(board[j][i] == symbol for j in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False

def read_coordinates(board):
    while True:
        try:
            coordinates = input("Enter the coordinates: ").split()
            x, y = map(int, coordinates)
            if not (1 <= x <= 3 and 1 <= y <= 3):
                print("Coordinates should be from 1 to 3!")
            elif board[x - 1][y - 1] != '_':
                print("This cell is occupied! Choose another one!")
            else:
                return x, y
        except ValueError:
            print("You should enter numbers!")

def main():
    # Ініціалізуємо порожню ігрову сітку
    board = [['_' for _ in range(3)] for _ in range(3)]

    # Виводимо порожню ігрову сітку на початку гри
    print_board(board)

    # Головний ігровий цикл
    while True:
        # Перший гравець (X)
        x, y = read_coordinates(board)
        board[x - 1][y - 1] = 'X'
        print_board(board)
        result = analyze_board(board)
        if result != "Game not finished":
            print(result)
            break

        # Другий гравець (O)
        x, y = read_coordinates(board)
        board[x - 1][y - 1] = 'O'
        print_board(board)
        result = analyze_board(board)
        if result != "Game not finished":
            print(result)
            break

if __name__ == "__main__":
    main()
