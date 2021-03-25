from collections import deque
water = int(input())
names_queue = deque()
name = input()

while name != "Start":
    names_queue.append(name)
    name = input()
command = input()
while command != "End":
    command = command.split()
    if command[0] == "refill":
        liters = int(command[1])
        water += liters
    else:
        liters = int(command[0])
        if water - liters >= 0:
            person_name = names_queue.popleft()
            print(f"{person_name} got water")
            water -= liters
        else:
            person_name = names_queue.popleft()
            print(f"{person_name} must wait")
    command = input()

print(f"{water} liters left")