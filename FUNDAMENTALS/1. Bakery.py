elements = input().split(" ")
dict = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i +1])
    dict[key] = value

print(dict)