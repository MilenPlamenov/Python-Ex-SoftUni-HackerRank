city = input().split(", ")
capital = input().split(", ")
dict = {}
for city,capital in zip(city,capital):
    dict[city] = capital

for k,v in dict.items():
    print(f"{k} -> {v}")