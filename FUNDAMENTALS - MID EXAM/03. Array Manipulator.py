import sys


def index_is_valid(arr, index):
    if 0 <= index < len(arr):
        return True
    return False


def exchange_command(array, idx):
    if index_is_valid(array, idx):
        n = array[idx + 1:]
        del array[idx + 1:]
        for i in reversed(n):
            array.insert(0, i)
    else:
        print("Invalid index")


def max_index_in_array(array, command):
    max_el = -sys.maxsize
    found = False
    index_of_max_el = 0
    if command == "odd":
        for i in range(len(array)):
            if array[i] % 2 != 0:
                if array[i] >= max_el:
                    max_el = array[i]
                    index_of_max_el = i
                    found = True
    elif command == "even":
        for i in range(len(array)):
            if array[i] % 2 == 0:
                if array[i] >= max_el:
                    max_el = array[i]
                    index_of_max_el = i
                    found = True

    if found:
        print(index_of_max_el)
    else:
        print("No matches")


def min_index_in_array(array, command):
    min_el = sys.maxsize
    found = False
    index_of_min_el = 0
    if command == "odd":
        for i in range(len(array)):
            if array[i] % 2 != 0:
                if array[i] <= min_el:
                    min_el = array[i]
                    index_of_min_el = i
                    found = True
    elif command == "even":
        for i in range(len(array)):
            if array[i] % 2 == 0:
                if array[i] <= min_el:
                    min_el = array[i]
                    index_of_min_el = i
                    found = True
    if found:
        print(index_of_min_el)
    else:
        print("No matches")


def find_first_count(array, command, counter):
    if counter > len(array):
        print("Invalid count")
    else:
        if command == "odd":
            new_list = []
            for el in array:
                if el % 2 != 0:
                    new_list.append(el)
                if len(new_list) == counter:
                    break
            print(new_list)
        elif command == "even":
            new_list = []
            for el in array:
                if el % 2 == 0:
                    new_list.append(el)
                if len(new_list) == counter:
                    break
            print(new_list)


def find_last_count(array, command, counter):
    if counter > len(array):
        print("Invalid count")
    else:
        if command == "odd":
            new_list = []
            for el in reversed(array):
                if el % 2 != 0:
                    new_list.append(el)
                if len(new_list) == counter:
                    break
            print(new_list)
        elif command == "even":
            new_list = []
            for el in reversed(array):
                if el % 2 == 0:
                    new_list.append(el)
                if len(new_list) == counter:
                    break
            print(new_list)


array = [int(i) for i in input().split()]
command = input()
while command != "end":
    command = command.split()
    if command[0] == "exchange":
        index = int(command[1])
        exchange_command(array, index)
    elif command[0] == "max":
        max_index_in_array(array, command[1])
    elif command[0] == "min":
        min_index_in_array(array, command[1])
    elif command[0] == "first":
        count = int(command[1])
        find_first_count(array, command[2], count)
    elif command[0] == "last":
        count = int(command[1])
        find_last_count(array, command[2], count)
    command = input()

print(array)
