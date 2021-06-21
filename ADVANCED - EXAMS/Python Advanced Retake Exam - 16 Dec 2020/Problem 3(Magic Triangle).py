def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for row in range(2, n):
        new_row = []
        for col in range(0, row + 1):
            if col - 1 < 0:
                new_row.append(1)
            elif col >= len(triangle[row - 1]):
                new_row.append(1)
            else:
                upper_left = triangle[row - 1][col - 1]
                upper_right = triangle[row - 1][col]
                new_value = upper_left + upper_right
                new_row.append(new_value)
        triangle.append(new_row)

    return triangle


print(get_magic_triangle(1))

#recursion


# def get_magic_triangle(n, a=[[1]]):
#     if n == 1:
#         return a
#
#     current = a[-1]
#     helper = []
#     for adding in range(len(a[-1]) + 1):
#         if adding in range(len(current)) and adding - 1 in range(len(current)):
#             add_sum = current[adding] + current[adding - 1]
#             helper.append(add_sum)
#         else:
#             helper.append(1)
#     a.append(helper)
#     return get_magic_triangle(n - 1, a)
#
#
# print(get_magic_triangle(5))