# On the first line of the input you will be given a text string. In order to win the competition
# you have to find all hidden word pairs, read them and mark the ones that are mirror images of each other.
# First of all you have to extract the hidden word pairs. Hidden word pairs are:
#     • Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
#     • At least 3 characters long each (without the surrounding symbols)
#     • Made up of letters only
# If the second word, spelled backwards is the same as the first word
# and vice versa (casing matters!), then they are a match and you have to store them somewhere.
#     • If you don`t find any valid pairs print: "No word pairs found!"
#     • If you find valid pairs print their count: "{valid pairs count} word pairs found!"
#     • If there are no mirror words print: "No mirror words!"
#     • If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, etc…"

import re
string_input = input()
mirror_words = []
final = []
pattern = r"#[A-Za-z]{3,}##[A-Za-z]{3,}#|@[A-Za-z]{3,}@@[A-Za-z]{3,}@"

matches = re.findall(pattern,string_input)
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
for word in matches:
    first_word = word[1:len(word)//2-1]
    second_word = word[len(word)//2+1:-1]
    if second_word[::-1] == first_word:
        mirror_words.append(first_word)

if mirror_words:
    print("The mirror words are:")
    for w in mirror_words:
        final.append(f"{w} <=> {w[::-1]}")
    print(", ".join(final))
else:
    print("No mirror words!")