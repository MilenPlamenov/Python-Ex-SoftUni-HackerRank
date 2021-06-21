first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
people_count = int(input())

total_eff_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours = 0
while people_count > 0:
    people_count -= total_eff_per_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1
        continue

print(f"Time needed: {hours}h.")