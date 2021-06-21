maximum_mana = 200
maximum_heal = 100
my_dict = {}
n = int(input())
for _ in range(n):
    hero_name, hp, mp = input().split()
    my_dict[hero_name] = [int(hp), int(mp)]

command = input()
while command != 'End':
    task_list = command.split(' - ')
    if task_list[0] == 'CastSpell':
        hero_name, mp_needed, spell_name = task_list[1:]
        mp_needed = int(mp_needed)
        if my_dict[hero_name][1] >= mp_needed:
            my_dict[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {my_dict[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif task_list[0] == 'TakeDamage':
        hero_name, dmg, attacker = task_list[1:]
        dmg = int(dmg)
        if my_dict[hero_name][0] > dmg:
            my_dict[hero_name][0] -= dmg
            print(f"{hero_name} was hit for {dmg} HP by {attacker} and now has {my_dict[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            my_dict.pop(hero_name)
    elif task_list[0] == 'Recharge':
        hero_name, amount = task_list[1:]
        amount = int(amount)
        if my_dict[hero_name][1] + amount >= maximum_mana:
            gain = maximum_mana - my_dict[hero_name][1]
        else:
            gain = amount
        my_dict[hero_name][1] += gain
        print(f"{hero_name} recharged for {gain} MP!")
    elif task_list[0] == 'Heal':
        hero_name, amount = task_list[1:]
        amount = int(amount)
        if my_dict[hero_name][0] + amount >= maximum_heal:
            gain = maximum_heal - my_dict[hero_name][0]
        else:
            gain = amount
        my_dict[hero_name][0] += gain
        print(f"{hero_name} healed for {gain} HP!")
    command = input()

for hero, hp_and_mana in sorted(my_dict.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{hero}")
    print(f'  HP: {hp_and_mana[0]}')
    print(f'  MP: {hp_and_mana[1]}')