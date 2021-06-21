data = input().split()

alphabet_positions = {chr(el + 97): el+1 for el in range(26)}
total_sum = 0
for element in data:
    first_letter = element[0]
    last_letter = element[-1]
    number = int(element[1:-1])
    if first_letter.isupper():
        number /= alphabet_positions[first_letter.lower()]
    elif first_letter.islower():
        number *= alphabet_positions[first_letter.lower()]

    if last_letter.isupper():
        number -= alphabet_positions[last_letter.lower()]
    elif last_letter.islower():
        number += alphabet_positions[last_letter.lower()]

    total_sum += number

print(f"{total_sum:.2f}")