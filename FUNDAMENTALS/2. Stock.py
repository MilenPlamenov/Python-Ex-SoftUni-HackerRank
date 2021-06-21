elements = input().split(" ")
dict = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i +1])
    dict[key] = value
serched_products = input().split()
for product in serched_products:
    if product in dict:
        print(f"We have {dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")