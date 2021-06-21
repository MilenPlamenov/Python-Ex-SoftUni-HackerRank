results = {}
count_submitions = {}

command = input()
while command != "exam finished":
    command = command.split("-")
    if command[1] == "banned":
        username = command[0]
        del results[username]
    else:
        username = command[0]
        language = command[1]
        points = int(command[2])
        if username not in results:
            results[username] = []
        results[username].append(points)

        if language not in count_submitions:
            count_submitions[language] = 1
        else:
            count_submitions[language] += 1

    command = input()
print("Results:")

for user, points in sorted(results.items(), key=lambda x:(x[1], -ord(x[0][0])), reverse=True):
    print(f"{user} | {max(points)}")

print("Submissions:")
for language, count in sorted(count_submitions.items(), key=lambda x:(-x[1], x[0])):
    print(f"{language} - {count}")
