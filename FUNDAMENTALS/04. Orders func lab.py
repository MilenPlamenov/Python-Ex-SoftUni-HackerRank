def orders_func(product, quantity, prc):
    if product == "coffee":
        prc = 1.50 * quantity
    elif product == "water":
        prc = 1. * quantity
    elif product == "coke":
        prc = 1.40 * quantity
    elif product == "snacks":
        prc = 2 * quantity
    return f"{prc:.2f}"


price = 0
product = input()
quantity = int(input())
res = orders_func(product, quantity, price)
print(res)
