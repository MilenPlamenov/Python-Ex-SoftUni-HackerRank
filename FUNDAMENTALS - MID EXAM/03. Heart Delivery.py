new_list = list(map(lambda x: int(x), input().split('@')))
valentines = 0
command = input()
jump_place = 0
while command != 'Love!':
    task = command.split()
    jump_index = int(task[1])
    jump_place += jump_index
    if jump_place in range(len(new_list)):
        if new_list[jump_place] == 0:
            print(f"Place {jump_place} already had Valentine's day.")
            command = input()
            continue
        new_list[jump_place] -= 2
        if new_list[jump_place] == 0:
            print(f"Place {jump_place} has Valentine's day.")
    else:
        jump_place = 0
        if new_list[0] == 0:
            print(f"Place {jump_place} already had Valentine's day.")
            command = input()
            continue
        new_list[0] -= 2
        if new_list[0] == 0:
            print(f"Place {jump_place} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {jump_place}.")
for place in new_list:
    if place != 0:
        valentines += 1
if valentines == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {valentines} places.")

