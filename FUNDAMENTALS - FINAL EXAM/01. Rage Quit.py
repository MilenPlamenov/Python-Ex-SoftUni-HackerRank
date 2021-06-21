line = input()
index = 0
blame = ""
lil_blame = ""
unique_symbols = 0
while index < len(line):
    if not line[index].isdigit():
        lil_blame += line[index].upper()
        index += 1
    else:
        num = ""
        while line[index].isdigit() and index < len(line):
            num += line[index]
            index += 1
        num = int(num)
        lil_blame = lil_blame.upper() * num
        blame += lil_blame

print(f"Unique symbols used: {len(set(blame))}")
print(blame)