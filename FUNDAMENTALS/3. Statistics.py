products = {}

command = input()

while command != "statistics":
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])

    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    command = input()
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
