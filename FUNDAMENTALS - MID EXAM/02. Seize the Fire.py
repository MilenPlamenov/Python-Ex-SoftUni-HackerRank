all_cells = input().split("#")
water = int(input())
effort = 0
fire = 0
cells = []

for cell in all_cells:
    current_cell = cell.split(" = ")
    type_of_fire = current_cell[0]
    cell = int(current_cell[1])

    if type_of_fire == "High":
        if not 81 <= cell <= 125:
            continue
    elif type_of_fire == "Medium":
        if not 51 <= cell <= 80:
            continue
    elif type_of_fire == "Low":
        if not 1 <= cell <= 50:
            continue
    if water < cell:
        continue
    water -= cell
    effort += cell * 0.25
    fire += cell
    cells.append(cell)

print("Cells:")
for cell in cells:
    print(f" - {cell}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire}")