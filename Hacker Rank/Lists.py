ll = []

for i in range(int(input())):
    command = input().split()
    if command[0] == "append":
        value = int(command[1])
        ll.append(value)
    elif command[0] == "insert":
        index = int(command[1])
        value = int(command[2])
        ll.insert(index, value)
    elif command[0] == "print":
        print(ll)
    elif command[0] == "remove":
        element = int(command[1])
        ll.remove(element)
    elif command[0] == "sort":
        ll.sort()
    elif command[0] == "pop":
        ll.pop()
    elif command[0] == "reverse":
        ll = ll[::-1]
