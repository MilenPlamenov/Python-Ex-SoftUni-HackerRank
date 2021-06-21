def smallest_of_three_nums(num_one, num_two, num_three, smallest_num):
    if num_one < smallest_num:
        smallest_num = num_one
    if num_two < smallest_num:
        smallest_num = num_two
    if num_three < smallest_num:
        smallest_num = num_three
    return smallest_num


smallest_num = 999999999999
num_o = int(input())
num_t = int(input())
num_thr = int(input())
res = smallest_of_three_nums(num_o, num_t, num_thr, smallest_num)
print(res)
