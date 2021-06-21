def snake_moves(mat, snake_r, snake_c):
    pass


rows = int(input())
matrix = []
for i in range(rows):
    row = list(input())
    matrix.append(row)
position_row = 0
position_col = 0
food_quantity = 0
game_over = False
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "S":
            position_row = row
            position_col = col
            break

while food_quantity < 10:
    command = input()
    size = len(matrix)
    if command == "down":
        if 0 <= position_row + 1 < size:
            matrix[position_row][position_col] = "."
            position_row += 1
            if matrix[position_row][position_col] == "*":
                food_quantity += 1
                matrix[position_row][position_col] = "."
            elif matrix[position_row][position_col] == "B":
                matrix[position_row][position_col] = "."
                for r in range(rows):
                    for c in range(rows):
                        if matrix[r][c] == "B":
                            matrix[r][c] = "S"
                            position_row = r
                            position_col = c
                            break
        else:
            game_over = True
            break
    elif command == "up":
        if 0 <= position_row - 1 < size:
            matrix[position_row][position_col] = "."
            position_row -= 1
            if matrix[position_row][position_col] == "*":
                food_quantity += 1
                matrix[position_row][position_col] = "."
            elif matrix[position_row][position_col] == "B":
                matrix[position_row][position_col] = "."
                for r in range(rows):
                    for c in range(rows):
                        if matrix[r][c] == "B":
                            matrix[r][c] = "S"
                            position_row = r
                            position_col = c
                            break
        else:
            game_over = True
            break
    elif command == "left":
        if 0 <= position_col - 1 < size:
            matrix[position_row][position_col] = "."
            position_col -= 1
            if matrix[position_row][position_col] == "*":
                food_quantity += 1

                matrix[position_row][position_col] = "."
            elif matrix[position_row][position_col] == "B":
                matrix[position_row][position_col] = "."
                for r in range(rows):
                    for c in range(rows):
                        if matrix[r][c] == "B":
                            matrix[r][c] = "S"
                            position_row = r
                            position_col = c
                            break
        else:
            game_over = True
            break

    elif command == "right":
        if 0 <= position_col + 1 < size:
            matrix[position_row][position_col] = "."
            position_col += 1
            if matrix[position_row][position_col] == "*":
                food_quantity += 1

                matrix[position_row][position_col] = "."
            elif matrix[position_row][position_col] == "B":
                matrix[position_row][position_col] = "."
                for r in range(rows):
                    for c in range(rows):
                        if matrix[r][c] == "B":
                            matrix[r][c] = "S"
                            position_row = r
                            position_col = c
                            break
        else:
            game_over = True
            break


if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
    matrix[position_row][position_col] = "S"
print(f"Food eaten: {food_quantity}")

for i in range(rows):
    row = list(map(str, matrix[i]))
    print(''.join(row))


# n = int(input())
# food_eaten = 0
# matrix = [[i for i in input()] for _ in range(n)]
#
# index = (0, 0)
# for row in range(n):
#     for col in range(n):
#         if matrix[row][col] == 'S':
#             index = [row, col]
#
# while True:
#     navigation = input()
#     current_index = index
#     matrix[current_index[0]][current_index[1]] = '.'
#
#     if navigation == 'left':
#         index[1] -= 1
#     elif navigation == 'right':
#         index[1] += 1
#     elif navigation == 'up':
#         index[0] -= 1
#     else:
#         index[0] += 1
#
#     if 0>index[0] or index[0]>=n or 0>index[1] or index[1]>=n:
#         print('Game over!')
#         break
#
#     if matrix[index[0]][index[1]] == '*':
#         food_eaten += 1
#     if food_eaten == 10:
#         print('You won! You fed the snake.')
#         matrix[current_index[0]][current_index[1]] = 'S'
#         break
#
#     elif matrix[index[0]][index[1]] == 'B':
#         for row in range(n):
#             for col in range(n):
#                 if matrix[row][col] == 'B' and (row != index[0] or row != index[1]):
#                     index = [row, col]
#                     matrix[index[0]][index[1]] = '.'
#
#
#
# print(f'Food eaten: {food_eaten}')
# [print(''.join(map(str, row))) for row in matrix]