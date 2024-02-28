import numpy as np

def read_matrix():
    n, m = map(int, input("Введіть розмір матриці: > ").split())
    print("Введіть матрицю:")
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix, n, m
def print_matrix(matrix):
    for row in matrix:
        print(*row)

def add_matrices():
    matrix1, n1, m1 = read_matrix()
    matrix2, n2, m2 = read_matrix()

    if n1 != n2 or m1 != m2:
        print("Матриці мають бути однакового розміру для додавання.")
        return

    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(m1)] for i in range(n1)]
    print("Результат:")
    print_matrix(result_matrix)

def multiply_matrix_by_constant():
    matrix, n, m = read_matrix()
    constant = float(input("Введіть константу: > "))

    result_matrix = [[matrix[i][j] * constant for j in range(m)] for i in range(n)]
    print("Результат:")
    print_matrix(result_matrix)

def multiply_matrices():
    matrix1, n1, m1 = read_matrix()
    matrix2, n2, m2 = read_matrix()

    if m1 != n2:
        print("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої матриці.")
        return

    result_matrix = np.dot(matrix1, matrix2)
    print("Результат:")
    print_matrix(result_matrix)

def transpose_main_diagonal(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed_matrix

def transpose_side_diagonal(matrix):
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix) - 1, -1, -1)] for i in range(len(matrix[0]) - 1, -1, -1)]
    return transposed_matrix

def transpose_vertical_line(matrix):
    transposed_matrix = [row[::-1] for row in matrix]
    return transposed_matrix

def transpose_horizontal_line(matrix):
    transposed_matrix = matrix[::-1]
    return transposed_matrix

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse_matrix(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return inv_matrix
    except np.linalg.LinAlgError:
        return None

if __name__ == "__main__":
    while True:
        print("1. Додавання матриць")
        print("2. Множення матриці на константу")
        print("3. Множення матриць")
        print("4. Транспонування матриці")
        print("5. Обчислення визначника")
        print("6. Обернена матриця")
        print("0. Вихід")
        choice = input("Ваш вибір: > ")

        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_matrix_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            print("1. Головна діагональ")
            print("2. Бічна діагональ")
            print("3. Вертикальна лінія")
            print("4. Горизонтальна лінія")
            transpose_choice = input("Ваш вибір: > ")

            matrix, n, m = read_matrix()

            if transpose_choice == "1":
                result_matrix = transpose_main_diagonal(matrix)
            elif transpose_choice == "2":
                result_matrix = transpose_side_diagonal(matrix)
            elif transpose_choice == "3":
                result_matrix = transpose_vertical_line(matrix)
            elif transpose_choice == "4":
                result_matrix = transpose_horizontal_line(matrix)
            else:
                print("Невірний вибір.")
                continue

            print("Результат:")
            print_matrix(result_matrix)
        elif choice == "5":
            matrix, n, m = read_matrix()

            if n != m:
                print("Матриця повинна бути квадратною для обчислення визначника.")
                continue

            det = determinant(matrix)
            print("Визначник:", det)
        elif choice == "6":
            matrix, n, m = read_matrix()

            if n != m:
                print("Матриця повинна бути квадратною для знаходження її оберненої.")
                continue

            inv_matrix = inverse_matrix(matrix)

            if inv_matrix is None:
                print("Ця матриця не має оберненої.")
            else:
                print("Результат:")
                print_matrix(inv_matrix)
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Будь ласка, введіть дійсну опцію.")
