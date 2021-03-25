from collections import deque
name = input()
names_queue = deque()
while name != "End":
    if name == "Paid":
        while names_queue:
            print(names_queue.popleft())
    else:
        names_queue.append(name)
    name = input()

print(f"{len(names_queue)} people remaining.")