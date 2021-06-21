data = list(map(int,input().split(" ")))
command = input()
temp = 0
while command != "End":
    index = int(command)
    if 0 <= index < len(data):
        temp = data[index]
        data[index] = -1
        for i in range(len(data)):
            if data[i] != -1:
                if data[i] > temp:
                    data[i] -= temp
                else:
                    data[i] += temp
    command = input()

print(f"Shot targets: {len([x for x in data if x == -1])} -> {' '.join([str(x) for x in data])}")