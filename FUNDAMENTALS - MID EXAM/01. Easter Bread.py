budget = float(input())
price_for_one_kg_flour = float(input())
easter_breads = 0
colored_eggs = 0
price_for_one_pack_of_eggs = price_for_one_kg_flour * 0.75
price_for_one_liter_milk = price_for_one_kg_flour + price_for_one_kg_flour * 0.25
price_for_milk_needed = price_for_one_liter_milk / 4


price_for_one_easter_bread = price_for_one_kg_flour + price_for_one_pack_of_eggs + price_for_milk_needed


while budget - price_for_one_easter_bread >= 0:
    budget -= price_for_one_easter_bread
    colored_eggs += 3
    easter_breads += 1
    if easter_breads % 3 == 0:
        colored_eggs -= easter_breads - 2

print(f"You made {easter_breads} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
