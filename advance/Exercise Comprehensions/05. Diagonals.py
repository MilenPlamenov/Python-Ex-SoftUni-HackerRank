rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(int, input().split(", ")))
    matrix.append(row)


sum_primary = 0
sum_secondary = 0
nums_primary = []
nums_sec = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            sum_primary += matrix[i][j]
            nums_primary.append(matrix[i][j])
            print()
        if (i + j) == (rows - 1):
            sum_secondary += matrix[i][j]
            nums_sec.append(matrix[i][j])

print(f"First diagonal: {', '.join([str(x) for x in nums_primary])}. Sum: {sum_primary}")
print((f"Second diagonal: {', '.join([str(x) for x in nums_sec])}. Sum: {sum_secondary}"))