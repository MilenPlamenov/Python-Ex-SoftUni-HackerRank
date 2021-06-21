new_dect = {}

command = input()
while command != "Log out":
    command = command.split(": ")
    check_about_username = True
    user = command[1]
    if user in new_dect:
        check_about_username = False
    if command[0] == "New follower":
        if check_about_username:
            new_dect[user] = [0, 0] #likes, comments
    elif command[0] == "Like":
        count_like = int(command[2])
        if check_about_username:
            new_dect[user] = [count_like, 0]
        else:
            new_dect[user][0] += count_like
    elif command[0] == "Comment":
        if check_about_username:
            new_dect[user] = [0, 1]
        else:
            new_dect[user][1] += 1
    elif command[0] == "Blocked":
        if check_about_username:
            print(f"{user} doesn't exist.'")
        else:
            del new_dect[user]
    command = input()

print(f'{len(new_dect)} followers')
for user, likes_and_comments in sorted(new_dect.items(), key=lambda x: (-(x[1][0] + x[1][1]), x[0])):
    print(f'{user}: {likes_and_comments[0] + likes_and_comments[1]}')