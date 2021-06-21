dictionary = {}

command = input()
while command != "stop":
    element = command
    quantity = int(input())
    if element not in dictionary:
        dictionary[element] = quantity
    else:
        dictionary[element] += quantity
    command = input()

for key, value in dictionary.items():
    print(f"{key} -> {value}")