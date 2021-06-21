capacity = int(input())
command = input()
money_paid = 0
total_joined_people = 0
total_money_paid = 0
is_full = False
while command != "Movie time!":
    joining_people = int(command)
    if total_joined_people >= capacity:
        is_full = True
        break
    money_paid = joining_people * 5
    if joining_people % 3 == 0:
        money_paid -= 5
    total_joined_people += joining_people
    total_money_paid += money_paid
    command = input()
if is_full:
    print("The cinema is full.")
else:
    seats_left = capacity - total_joined_people
    print(f"There are {seats_left} seats left in the cinema.")

print(f"Cinema income - {total_money_paid} lv.")
