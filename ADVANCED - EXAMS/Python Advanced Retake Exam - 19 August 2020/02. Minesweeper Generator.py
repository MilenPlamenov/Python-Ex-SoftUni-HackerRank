def minesweeper_func(mat, r, c):
    if 0 <= r < len(mat) and 0 <= c - 1 < len(mat):
        if mat[r][c - 1] != "*":
            mat[r][c - 1] += 1
    if 0 <= r - 1 < len(mat) and 0 <= c - 1 < len(mat):
        if mat[r - 1][c - 1] != "*":
            mat[r - 1][c - 1] += 1
    if 0 <= r - 1 < len(mat) and 0 <= c < len(mat):
        if mat[r - 1][c] != "*":
            mat[r - 1][c] += 1
    if 0 <= r - 1 < len(mat) and 0 <= c + 1 < len(mat):
        if mat[r - 1][c + 1] != "*":
            mat[r - 1][c + 1] += 1
    if 0 <= r < len(mat) and 0 <= c + 1 < len(mat):
        if mat[r][c + 1] != "*":
            mat[r][c + 1] += 1
    if 0 <= r + 1 < len(mat) and 0 <= c + 1 < len(mat):
        if mat[r + 1][c + 1] != "*":
            mat[r + 1][c + 1] += 1
    if 0 <= r + 1 < len(mat) and 0 <= c < len(mat):
        if mat[r + 1][c] != "*":
            mat[r + 1][c] += 1
    if 0 <= r + 1 < len(mat) and 0 <= c - 1 < len(mat):
        if mat[r + 1][c - 1] != "*":
            mat[r + 1][c - 1] += 1


rows = int(input())
matrix = [[0] * rows for _ in range(rows)]

bombs = int(input())

for i in range(bombs):
    position = input().split(', ')
    bomb_row = int(position[0].strip('()'))
    bomb_col = int(position[1].strip('()'))
    matrix[bomb_row][bomb_col] = "*"

# deltas = [
#     (0, -1),
#     (-1, -1),
#     (-1, 0),
#     (-1, +1),
#     (0, +1),
#     (+1, +1),
#     (+1, 0),
#     (+1, -1)
# ]

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == "*":
            minesweeper_func(matrix, row, col)


for i in range(rows):
    row = list(map(str, matrix[i]))
    print(' '.join(row))
