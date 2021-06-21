import re

pattern = r"\d+"


data = input()


matches = re.findall(pattern, data)
print(" ".join(matches))