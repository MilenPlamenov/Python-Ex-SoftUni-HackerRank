inventory = {
    hero: {
        'items': [],
        'total_cost': 0
    }
    for hero in input().split(', ')
}

command = input()
while command != "End":
    name, item, cost = command.split('-')
    if item not in inventory[name]['items']:
        inventory[name]['items'].append(item)
        inventory[name]['total_cost'] += int(cost)

    command = input()

for name, value in inventory.items():
    print(f'{name} -> Items: {len(value["items"])}, Cost: {value["total_cost"]}')