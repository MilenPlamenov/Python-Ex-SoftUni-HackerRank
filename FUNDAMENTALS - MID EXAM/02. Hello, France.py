collection_of_items = input().split('|')
budget = float(input())
profit = 0
new_collection = []
final_collection = []
for item in collection_of_items:
    items = item.split("->")
    type_of_item = items[0]
    price = float(items[1])
    if budget < price:
        continue
    if type_of_item == "Clothes":
        if price <= 50.00:
            budget -= price
            new_collection.append(price)
    elif type_of_item == "Shoes":
        if price <= 35.00:
            budget -= price
            new_collection.append(price)
    elif type_of_item == "Accessories":
        if price <= 20.50:
            budget -= price
            new_collection.append(price)


for price in new_collection:
    price += price * 0.4
    final_collection.append(price)
    print(f"{price:.2f}", end=" ")

profit = sum(new_collection) * 0.4
print(f"\nProfit: {profit:.2f}")

if budget + sum(final_collection) < 150:
    print("Time to go.")
else:
    print("Hello, France!")