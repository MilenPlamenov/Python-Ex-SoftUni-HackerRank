# Your task is to write program which extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# An emoji is valid when:
#     • Is surrounded by either :: or ** (exactly 2)
#     • Is at least 3 characters long (without the surrounding symbols)
#     • Starts with a capital letter
#     • Continues with lowercase letters only
# You need to print the result of cool threshold and after that to take all emojis out of the text, count them
# and print the only the cool ones on the console.

import re

text = input()
cool_emoji = []
cool_threshold = 1
total_emoji = 0
for digit in text:
    if digit.isdigit():
        cool_threshold *= int(digit)

pattern = r"(::|(?<=::))[A-Z][a-z]{2,}(::|(?=::))|(\*{2}|(?<=\*{2}))[A-Z][a-z]{2,}(\*{2}|(?=\*{2}))"

for match in re.finditer(pattern, text):
    total_sum = 0
    total_emoji += 1
    for letter in match.group():
        if letter != "*" and letter != ":":
            total_sum += ord(letter)
    if total_sum >= cool_threshold:
        cool_emoji.append(match.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{total_emoji} emojis found in the text. The cool ones are:")
for i in cool_emoji:
    print(i, end="\n")