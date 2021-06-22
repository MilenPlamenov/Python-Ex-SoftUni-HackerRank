def valid_coordinates(func_matrix, row_n, col_n):
    if 0 <= row_n < len(func_matrix):
        if 0 <= col_n < len(func_matrix):
            return True
    return False


def add_to_the_matrix(func_matrix, row_n, col_n, value_to_change):
    if valid_coordinates(func_matrix, row_n, col_n):
        func_matrix[row_n][col_n] += value_to_change
        return func_matrix
    print("Invalid coordinates")
    return func_matrix


def subtract_from_the_matrix(func_matrix, row_n, col_n, value_to_change):
    if valid_coordinates(func_matrix, row_n, col_n):
        func_matrix[row_n][col_n] -= value_to_change
        return func_matrix
    print("Invalid coordinates")
    return func_matrix


def print_res(matrix_func):
    for x in range(rows):
        r = list(map(str, matrix_func[x]))
        print(' '.join(r))


rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(int, input().split(" ")))
    matrix.append(row)

command = input()
while command != "END":
    command = command.split(" ")
    row_of_command = int(command[1])
    col_of_command = int(command[2])
    value = int(command[3])
    if command[0] == "Add":
        add_to_the_matrix(matrix, row_of_command, col_of_command, value)
    elif command[0] == "Subtract":
        subtract_from_the_matrix(matrix, row_of_command, col_of_command, value)
    command = input()

print_res(matrix)
