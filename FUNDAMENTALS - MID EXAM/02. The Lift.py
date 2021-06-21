people = int(input())
wagons = input().split()
wagons_list = [int(wagons[c])for c in range(len(wagons))]
for fill in range(len(wagons_list)):
    if people < 4:
        wagons_list[fill] += people
        people = 0
        break
    else:
        people -= 4 - wagons_list[fill]
        wagons_list[fill] += 4 - wagons_list[fill]

for_list = [c for c in wagons_list if c == 4]
wagons_list = [str(el) for el in wagons_list]
if len(for_list) != len(wagons_list):
    print("The lift has empty spots!")
    print(" ".join(wagons_list))
elif people > 0 and len(for_list) == len(wagons_list):
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(wagons_list))
else:
    print(" ".join(wagons_list))