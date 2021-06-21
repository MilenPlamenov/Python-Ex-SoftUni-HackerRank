import numpy


rows = int(input())
matrix = []

for i in range(rows):
    row = list(map(float, input().split(" ")))
    matrix.append(row)

if numpy.linalg.det(matrix) != 0: #and numpy.linalg.det(matrix) != 6:
    print(f"{numpy.linalg.det(matrix):.2f}")
else:
    print(numpy.linalg.det(matrix))