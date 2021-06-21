str_input = input()

rows = int(input())
matrix = []
position_row = 0
position_col = 0
for i in range(rows):
    row = list(input())
    matrix.append(row)

for r in range(rows):
    for c in range(rows):
        if matrix[r][c] == "P":
            position_row = r
            position_col = c
            break

for i in range(int(input())):
    command = input()
    size = len(matrix)
    if command == "down":
        if 0 <= position_row + 1 < size:
            matrix[position_row][position_col] = "-"
            position_row += 1
            if matrix[position_row][position_col] != "-":
                str_input += matrix[position_row][position_col]
                matrix[position_row][position_col] = "P"
        else:
            if len(str_input) > 0:
                last_letter = str_input[-1]
                str_input = str_input[::-1].replace(last_letter, "", 1)
                str_input = str_input[::-1]

    elif command == "up":
        if 0 <= position_row - 1 < size:
            matrix[position_row][position_col] = "-"
            position_row -= 1
            if matrix[position_row][position_col] != "-":
                str_input += matrix[position_row][position_col]
                matrix[position_row][position_col] = "P"
        else:
            if len(str_input) > 0:
                last_letter = str_input[-1]
                str_input = str_input[::-1].replace(last_letter, "", 1)
                str_input = str_input[::-1]

    elif command == "left":
        if 0 <= position_col - 1 < size:
            matrix[position_row][position_col] = "-"
            position_col -= 1
            if matrix[position_row][position_col] != "-":
                str_input += matrix[position_row][position_col]
                matrix[position_row][position_col] = "P"
        else:
            if len(str_input) > 0:
                last_letter = str_input[-1]
                str_input = str_input[::-1].replace(last_letter, "", 1)
                str_input = str_input[::-1]
    elif command == "right":
        if 0 <= position_col + 1 < size:
            matrix[position_row][position_col] = "-"
            position_col += 1
            if matrix[position_row][position_col] != "-":
                str_input += matrix[position_row][position_col]
                matrix[position_row][position_col] = "P"
        else:
            if len(str_input) > 0:
                last_letter = str_input[-1]
                str_input = str_input[::-1].replace(last_letter, "", 1)
                str_input = str_input[::-1]


print(str_input)

for i in range(rows):
    row = list(map(str, matrix[i]))
    print(''.join(row))