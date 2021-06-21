capacity = int(input())
price_per_ticket = 5
total_money = 0
command = input()
is_Full = False
total_entered_people = 0
while command != "Movie time!":
    entering_people = int(command)
    price_tickets = price_per_ticket * entering_people
    if entering_people % 3 == 0:
        price_tickets -= 5
    total_entered_people += entering_people
    if total_entered_people > capacity:
        is_Full = True
        break
    total_money += price_tickets

    command = input()
seats_left = capacity - total_entered_people
if is_Full:
    print("The cinema is full.")
else:
    print(f"There are {abs(seats_left)} seats left in the cinema.")

print(f"Cinema income - {total_money} lv.")