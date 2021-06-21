product_price = {}
product_quantity = {}

command = input()
while command != "buy":
    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    if product not in product_price:
        product_price[product] = price
        product_quantity[product] = quantity
    else:
        product_price[product] = price
        product_quantity[product] += quantity

    command = input()

for product, price in product_price.items():
    total_price = product_price[product] * product_quantity[product]
    print(f"{product} -> {total_price:.2f}")
