import math
biscuits_per_day = int(input())
workers = int(input())
number_of_biscuits_per_month = int(input())
total_biscuits_per_day = biscuits_per_day * workers
final_biscuits = 0
for day in range(1, 30+1):
    if day % 3 == 0:
        final_biscuits += math.floor(total_biscuits_per_day * 0.75)
    else:
        final_biscuits += total_biscuits_per_day

print(f"You have produced {int(final_biscuits)} biscuits for the past month.")

if final_biscuits > number_of_biscuits_per_month:
    diff = final_biscuits - number_of_biscuits_per_month
    print(f"You produce {diff / number_of_biscuits_per_month * 100:.2f} percent more biscuits.")
else:
    diff = abs(final_biscuits - number_of_biscuits_per_month)
    print(f"You produce {(diff / number_of_biscuits_per_month) * 100:.2f} percent less biscuits.")

