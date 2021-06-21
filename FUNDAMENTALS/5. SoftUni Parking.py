n = int(input())
command = input()
user_plates = {}
while True:
    command = command.split()
    if command[0] == "register":
        user = command[1]
        plate_number = (command[2])
        if user not in user_plates:
            user_plates[user] = plate_number
            print(f"{user} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {user_plates[user]}")

    elif command[0] == "unregister":
        username = command[1]
        if username not in user_plates:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            user_plates.pop(username)
    n -= 1
    if n == 0:
        break
    command = input()

for user, plate in user_plates.items():
    print(f"{user} => {plate}")