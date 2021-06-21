total_sum = 0
tax = 0
final_price = 0
command = input()

while True:
    part = float(command)
    if command == "regular":
        break
    elif command == "special":
        break
    else:
        if part < 0:
            print(f"Invalid price!")
            command = input()
            continue
    total_sum += part
    tax += part * 0.2

    command = input()
print(total_sum)
print(tax)
