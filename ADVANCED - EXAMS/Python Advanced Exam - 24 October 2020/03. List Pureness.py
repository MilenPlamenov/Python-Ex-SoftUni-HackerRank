def best_list_pureness(l_of_nums, rotations):
    biggest_sum = 0
    best_rotation = 0
    rotations = min(len(l_of_nums), rotations)
    for i in range(rotations + 1):
        current_sum = 0
        for (index, value) in enumerate(l_of_nums):
            current_sum += index * value
        if biggest_sum < current_sum:
            biggest_sum = current_sum
            best_rotation = i
        l_of_nums = l_of_nums[-1:] + l_of_nums[:-1]
    return f"Best pureness {biggest_sum} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


# def best_list_pureness(*args):
#     args = list(args)
#     l_of_nums = args
#     rotations = l_of_nums.pop()
#     l_of_nums = args[0]
#     biggest_sum = -9999999999
#     best_rotation = 0
#     for i in range(rotations + 1):
#         current_sum = 0
#         for index in range(len(l_of_nums)):
#             current_sum += l_of_nums[index] * index
#         if biggest_sum < current_sum:
#             biggest_sum = current_sum
#             best_rotation = i
#         l_of_nums = l_of_nums[-1:] + l_of_nums[:-1]
#     return f"Best pureness {biggest_sum} after {best_rotation} rotations"