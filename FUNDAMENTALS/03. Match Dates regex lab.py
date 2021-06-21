import re
data = input()

pattern = r"(?P<date>[0-9]{2})([\.\/-])(?P<month>[A-Z][a-z]{2})\2(?P<year>[0-9]{4})"

matches = re.finditer(pattern, data)

for match in matches:
    obj = match.group(0)
    day = obj[0:2]
    month = obj[3:6]
    year = obj[7::]
    print(f"Day: {day}, Month: {month}, Year: {year}")