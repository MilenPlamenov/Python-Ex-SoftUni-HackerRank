# def get_deltas(mat, kings_r, kings_c, deltas):
#     (delta_r, delta_c) = deltas
#     while True:
#         if not 0 <= delta_r < len(mat) or 0 <= delta_c < len(mat):
#             return None
#
#         if mat[kings_r][kings_c] == "Q":
#             return (kings_r, kings_c)
#
#         kings_r += delta_r
#         kings_c += delta_c
#
#
# def capture_with_deltas(mat, kings_r, kings_c):
#     deltas = [
#         (0, -1),
#         (-1, -1),
#         (-1, 0),
#         (-1, +1),
#         (0, +1),
#         (+1, +1),
#         (+1, 0),
#         (+1, -1)
#     ]
#     queens = [
#         get_deltas(mat, kings_r, kings_c, deltas)
#         for delta in deltas
#     ]
#     return [queen for queen in queens if queen]
#
#
# def print_res(queens):
#     if queens:
#         for queen in queens:
#             print(queen)
#     else:
#         print("The king is safe")
#
#
# matrix = []
# kings_row = 0
# kings_col = 0
# for i in range(8):
#     row = list(input().split(" "))
#     matrix.append(row)
#
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         if matrix[row][col] == "K":
#             kings_row = row
#             kings_col = col
#
# queens = capture_with_deltas(matrix, kings_row, kings_col)
# print_res(queens)

def king_position(m):
    position = []
    for r in range(8):
        for c in range(8):
            if m[r][c] == "K":
                position = [r, c]
    return position


matrix = [list(input().split()) for row in range(8)]
king = king_position(matrix)


def check_horizontal(m, k):
    current_left_queen_pos = []
    current_right_queen_pos = []
    queens = []
    for c in range(k[1]):
        if m[k[0]][c] == "Q":
            current_left_queen_pos.append(c)
    for c in range(k[1] + 1, 8):
        if m[k[0]][c] == "Q":
            current_right_queen_pos.append(c)
    if current_left_queen_pos:
        queens.append([k[0], max(current_left_queen_pos)])
    if current_right_queen_pos:
        queens.append([k[0], min(current_right_queen_pos)])
    return queens


def check_vertical(m, k):
    current_upper_queen_pos = []
    current_lower_queen_pos = []
    queens = []
    for r in range(k[0]):
        if m[r][k[1]] == "Q":
            current_upper_queen_pos.append(r)
    for r in range(k[0] + 1, 8):
        if m[r][k[1]] == "Q":
            current_lower_queen_pos.append(r)
    if current_upper_queen_pos:
        queens.append([max(current_upper_queen_pos), k[1]])
    if current_lower_queen_pos:
        queens.append([min(current_lower_queen_pos), k[1]])
    return queens


def left_diagonal(m, k):
    current_upper_queen = []
    current_lower_queen = []
    queens = []
    i = 0
    j = 0
    while True:
        i += 1
        if m[k[0] - i][k[1] - i] == "Q":
            current_upper_queen.append([k[0] - i, k[1] - i])
        if k[0] - i == 0 or k[1] - i == 0:
            if current_upper_queen:
                queens.append(max(current_upper_queen))
            break
    while True:
        j += 1
        if m[k[0] + j][k[1] + j] == "Q":
            current_lower_queen.append([k[0] + j, k[1] + j])
        if k[0] + j == 7 or k[1] + j == 7:
            if current_lower_queen:
                queens.append(min(current_lower_queen))
            break
    return queens


def right_diagonal(m, k):
    current_upper_queen = []
    current_lower_queen = []
    queens = []
    i = 0
    j = 0
    while True:
        i += 1
        if m[k[0] - i][k[1] + i] == "Q":
            current_upper_queen.append([k[0] - i, k[1] + i])
        if k[0] - i == 0 or k[1] + i == 7:
            if current_upper_queen:
                queens.append(current_upper_queen[0])
            break
    while True:
        j += 1
        if m[k[0] + j][k[1] - j] == "Q":
            current_lower_queen.append([k[0] + j, k[1] - j])
        if k[0] + j == 7 or k[1] - j == 0:
            if current_lower_queen:
                queens.append(current_lower_queen[0])
            break
    return queens


result = right_diagonal(matrix, king) + left_diagonal(matrix, king) + \
         check_horizontal(matrix, king) + check_vertical(matrix, king)

if result:
    print(*result, sep="\n")
else:
    print(f"The king is safe!")