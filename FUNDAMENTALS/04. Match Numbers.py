import re

data = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
mathes = re.finditer(pattern, data)

for match in mathes:
    print(match.group(0),end=" ")