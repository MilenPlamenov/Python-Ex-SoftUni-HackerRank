total_sum = 0
tax = 0
final_price = 0
final_price_is_zero = False
command = input()
while command != "special" and command != "regular":

    prices_parts = float(command)
    if prices_parts < 0:
        print(f"Invalid price!")
        command = input()
        continue

    total_sum += prices_parts
    tax += prices_parts * 0.2

    command = input()

final = tax + total_sum
if command == "special":
    final = final - final * 0.1

if final > 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_sum:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {final:.2f}$")
else:
    print("Invalid order!")