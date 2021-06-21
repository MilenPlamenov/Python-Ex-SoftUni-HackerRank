def numbers_searching(*args):
    missing_number = 0
    list_of_numbers = list(args)
    set_of_duplicates = set([x for x in list_of_numbers if list_of_numbers.count(x) > 1])
    list_of_duplicates = sorted(list(set_of_duplicates))
    for x in sorted(list_of_numbers):
        if x + 1 not in list_of_numbers:
            missing_number = x + 1
            break
    return [missing_number, list_of_duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))