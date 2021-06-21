array = [int(i) for i in input().split()]

average = sum(array) / len(array)
new_array = []

for num in array:
    if num > average:
        new_array.append(num)


if len(new_array) < 1:
    print("No")
else:
    new_array.sort(reverse=True)

    final_array = new_array[:5]
    final_array = [str(i) for i in final_array]
    print(" ".join(final_array))