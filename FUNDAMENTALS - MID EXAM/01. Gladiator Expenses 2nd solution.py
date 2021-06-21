lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = 0
broken_swords = 0
broken_shields = 0
broken_armors = 0

for lost in range(1, lost_fights + 1):
    if lost % 2 == 0:
        broken_helmets += 1
    if lost % 3 == 0:
        broken_swords += 1

    if lost % 6 == 0:
        broken_shields += 1

    if lost % 12 == 0:
        broken_armors += 1

helmet_expenses = broken_helmets * helmet_price
sword_expenses = broken_swords * sword_price
shield_expenses = broken_shields * shield_price
armor_expenses = broken_armors * armor_price

total_expenses = helmet_expenses + sword_expenses + shield_expenses + armor_expenses
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
