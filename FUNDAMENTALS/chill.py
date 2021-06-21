# enumerate
# names = ["Peter", "Gosho", "Pesho", "Sasho"]
#
# for index, name in enumerate(names, start=0):  # <-optional start=n
#     print(index, name)

# zip

# names_of_heroes = ["Peter Parker", "Clark Kent"]
# heroes = ["Spiderman", "Superman"]
# universe = ["Marvel", "DC"]
#
# for name_hero, hero, universe in zip(names_of_heroes, heroes, universe):
#     print(f"{name_hero} is actually {hero} from {universe}")

# unpacking

# a, b, *_ = (1, 2, 3, 4, 5)
# print(a)
# print(b)
#unpacking with *
# w, x, *y, z = (1, 2, 3, 4, 5, 6, 7)  # the * will take all other values
# print(w)
# print(x)
# print(y)
# print(z)
#
# from getpass import getpass
# username = input()
# password = getpass()


# nums = [1, 2, 3]
#
# i_nums = iter(nums)
# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break



# nums = [3, 4, 5, 6, 10, 2222, 1, -1, -223124, 34]
# nums.sort()
# print(nums[1]) # second lowest number
# print(nums[-2]) # second highest number

marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))