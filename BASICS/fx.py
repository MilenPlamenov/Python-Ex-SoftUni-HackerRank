name = input()
count_games = int(input())
points = 0
wins = 0
draws = 0
loses = 0


for games in range(1, count_games + 1):
    game = input()
    if count_games >= 1:
        if game == "W":
            points += 3
            wins += 1
        elif game == "D":
            points += 1
            draws +=1
        elif game == "L":
            points += 0
            loses += 1
print(f"{name} has won {points} points during this season.")
print("Total stats:")
print(f"## W: {wins}")
print(f"## D: {draws}")
print(f"## L: {loses}")
print(f"Win rate: {wins / count_games * 100:.2f}%")


if count_games == 0:
    print(f"{name} hasn't played any games during this season")
#print(f"{name} has won {points} points during this season.")
#print("Total stats:")
#print(f"## W: {wins}")
#print(f"## D: {draws}")
#print(f"## L: {loses}")
#print(f"Win rate: {wins / count_games * 100:.2f}%")

