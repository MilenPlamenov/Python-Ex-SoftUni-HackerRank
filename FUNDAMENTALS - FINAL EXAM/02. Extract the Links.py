import re
text = input()
pattern = r"(^|(?<=\s))www\.[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))"
while text:
    for match in re.finditer(pattern, text):
        print(match.group())
    text = input()


