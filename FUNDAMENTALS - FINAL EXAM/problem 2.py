import re
num = int(input())

pattern = r"^(.+)>(\d+)\|([a-z]+)\|([A-Z]+)\|([^<>]\S+[^<>])<\1$"

for i in range(num):
    text = input()
    res = re.match(pattern, text)
    if res:
        password = res[2] + res[3] + res[4] + res[5]
        print(f"Password: {password}")
    else:
        print("Try another password!")