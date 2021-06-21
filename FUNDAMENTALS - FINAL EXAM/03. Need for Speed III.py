n = int(input())

my_dict = {}
for _ in range(n):
    car, mileage, fuel = input().split("|") # mileage - 0 index fuel - 1 index
    my_dict[car] = [int(mileage), int(fuel)]

command = input()
while command != "Stop":
    command = command.split(" : ")
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if my_dict[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            my_dict[car][0] += distance
            my_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if my_dict[car][0] >= 100000:
                my_dict.pop(car)
                print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        gain = 0
        if my_dict[car][1] + fuel > 75:
            gain = 75 - my_dict[car][1]
            my_dict[car][1] += gain
        else:
            gain = fuel
            my_dict[car][1] += fuel
        print(f"{car} refueled with {gain} liters")
    elif command[0] == "Revert":
        car = command[1]
        mileage = int(command[2])
        if my_dict[car][0] - mileage < 10000:
            my_dict[car][0] = 10000
        else:
            my_dict[car][0] -= mileage
            print(f"{car} mileage decreased by {mileage} kilometers")

    command = input()

for car,mileage in sorted(my_dict.items(), key=lambda x: (x[1], -ord(x[0][0])), reverse=True):
    print(f"{car} -> Mileage: {my_dict[car][0]} kms, Fuel in the tank: {my_dict[car][1]} lt.")