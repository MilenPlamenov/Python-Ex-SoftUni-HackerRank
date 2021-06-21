from collections import deque

bomb_effects = deque([int(i) for i in input().split(", ")])
bomb_casings = [int(i) for i in input().split(", ")]

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
filled_bomb_pouch = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        filled_bomb_pouch = True
        break
    if current_casing + current_effect == 40:
        datura_bombs += 1
        bomb_casings.pop()
        bomb_effects.popleft()
    elif current_casing + current_effect == 60:
        cherry_bombs += 1
        bomb_casings.pop()
        bomb_effects.popleft()
    elif current_casing + current_effect == 120:
        smoke_decoy_bombs += 1
        bomb_casings.pop()
        bomb_effects.popleft()
    else:
        bomb_casings[-1] -= 5


if filled_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(ef) for ef in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(cas) for cas in bomb_casings])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
