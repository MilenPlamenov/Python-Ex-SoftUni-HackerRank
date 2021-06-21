def list_manipulator(*args):
    nums = args[0]
    commands = list(args[1:])
    if "add" in commands:
        if "beginning" in commands:
            new_ll = commands[2:]
            for num in reversed(new_ll):
                nums.insert(0, num)
            return nums
    if "add" in commands:
        if "end" in commands:
            new_ll = commands[2:]
            for num in new_ll:
                nums.append(num)
            return nums
    if "remove" in commands:
        if "beginning" in commands:
            if commands[2:]:
                for _ in range(commands[-1]):
                    nums.pop(0)
            else:
                nums.pop(0)
            return nums

    if "remove" in commands:
        if "end" in commands:
            if commands[2:]:
                for _ in range(commands[-1]):
                    nums.pop()
            else:
                nums.pop()
            return nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
