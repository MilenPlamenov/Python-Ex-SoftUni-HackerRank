n = int(input())
my_dict = {}
for i in range(n):
    piece, composer, key = input().split("|")
    my_dict[piece] = [composer, key] #0 index - composer #1 index - key

command = input()

while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in my_dict:
            my_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece not in my_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            del my_dict[piece]
    elif command[0] == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in my_dict:
            my_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece, composer in sorted(my_dict.items(), key=lambda x:(x[0], (x[1][0]))):
    print(f"{piece} -> Composer: {my_dict[piece][0]}, Key: {my_dict[piece][1]}")