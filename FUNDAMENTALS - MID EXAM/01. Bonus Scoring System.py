import math

count_students = int(input())
count_lectures = int(input())
initial_bonus = int(input())

max_bonus = 0
max_attendances = 0

for student in range(count_students):
    attendances = int(input())
    total_bonus = (attendances / count_lectures) * (5 + initial_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        max_attendances = attendances

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {max_attendances} lectures.")