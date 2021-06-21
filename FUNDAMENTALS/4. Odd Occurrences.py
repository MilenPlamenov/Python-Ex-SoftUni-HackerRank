words = input().split()

diction = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in diction:
        diction[word_lower] = 0
    diction[word_lower] += 1

for (key, value) in diction.items():
    if value % 2 != 0:
        print(key, end=" ")