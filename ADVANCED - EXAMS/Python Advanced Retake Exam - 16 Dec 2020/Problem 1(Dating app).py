from collections import deque

males = [int(i) for i in input().split(" ")]
females = deque([int(i) for i in input().split(" ")])

matches = 0


while females and males:
    current_male = males[-1] #stack
    current_female = females[0] #deque
    if current_male <= 0:
        males.pop()
    elif current_female <= 0:
        females.popleft()
    elif current_female == current_male:
        females.popleft()
        males.pop()
        matches += 1
    elif current_female % 25 == 0:
        females.popleft()
        females.popleft()
    elif current_male % 25 == 0:
        males.pop()
        if males:
            males.pop()
    else:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(reversed([str(m) for m in males]))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(f) for f in females])}")
else:
    print("Females left: none")