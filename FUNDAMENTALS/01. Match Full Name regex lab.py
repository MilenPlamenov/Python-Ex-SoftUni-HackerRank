import re
line = input()

pattern = r"^[A-Z][a-z]+\s[A-Z][a-z]+"

result = re.findall(pattern, line)

print(" ".join(result))