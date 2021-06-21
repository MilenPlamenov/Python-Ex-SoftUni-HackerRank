import re
total = 0
furniture = []
text = input()
pattern = r">>(?P<item>[A-Za-z]+)<<(?P<price>[0-9]+(\.[0-9]+)?)\!(?P<quantity>[0-9]+)"
while text != "Purchase":
    match = re.match(pattern, text)
    if match:
        data = match.groupdict()
        furniture.append(data["item"])
        total += float(data["price"]) * int(data["quantity"])
    text = input()
print("Bought furniture:")
if furniture:
    print(*furniture,sep="\n")
print(f"Total money spend: {total:.2f}")