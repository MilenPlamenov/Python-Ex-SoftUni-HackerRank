total_sum = 0
command = input()

while command != "NoMoreMoney":
    income = float(command)
    if income < 0:
        print(f"Invalid operation!")
        break
    total_sum += income
    print(f"Increase: {income:.2f}")

    command = input()

print(f"Total: {total_sum:.2f}")