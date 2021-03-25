from collections import deque

names = input().split(" ")
steps = int(input())
names_queue = deque(names)

i = 0
while len(names_queue) > 1:
    i += 1
    current = names_queue.popleft()
    if i == steps:
        print(f"Removed {current}")
        i = 0
    else:
        names_queue.append(current)

print(f"Last is {names_queue.popleft()}")