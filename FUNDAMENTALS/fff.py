biscuits = input().split(', ')
command = input()
while command != 'Eat':
    current_command = command.split()
    if current_command[0] == 'Update-Any':
        biscuit = current_command[1]
        if current_command[1] in biscuits:
            index = biscuits.index(biscuit)
            biscuits.remove(biscuit)
            biscuits.insert(index, 'Out of stock')

    if current_command[0] == 'Remove':
        biscuit = current_command[1]
        index = int(current_command[2])
        if 0 <= index < len(biscuits):
            biscuits[index] = biscuit
    if current_command[0] == 'Update-Last':
        biscuit = current_command[1]
        biscuits[-1] = biscuit

    if current_command[0] == 'Rearrange':
        if current_command[1] in biscuits:
            biscuits.remove(current_command[1])
            biscuits.append(current_command[1])

    command = input()

if 'Out of stock' in biscuits:
    biscuits.remove('Out of stock')
biscuits = [str(el) for el in biscuits]
print(' '.join(biscuits))