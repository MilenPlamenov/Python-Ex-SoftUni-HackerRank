# You will be given a string -> some places on the map. You have to filter only the valid ones. A valid location is:
#     • Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
#     • After the first "=" or "/" there should be only letters (the first must be upper-case)
#     • The letters must be at least 3
# After you have matched all the valid locations, you have to calculate travel points.
# They are calculated by summing the lengths of all the valid destinations that you have found on the map.
# At the end, on the first line print the following: "Destinations: {destinations joined by ', '}".
# On the second line print "Travel Points: {travel_points}".

import re
destinations = input()
points = 0
all_words = []
pattern = r"(?<=(/))[A-Z][A-Za-z]{2,}(?=(/))|(?<=(=))[A-Z][A-Za-z]{2,}(?=(=))"

for match in re.finditer(pattern, destinations):
    all_words.append(match.group())
if all_words:
    for word in all_words:
        new_word = ""
        for l in word:
            if l != "=" and l != "/":
                new_word += l
        points += len(new_word)

print(f'Destinations:', end=" ")
print(*all_words, sep=", ")
print(f"Travel Points: {points}")

