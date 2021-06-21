money = float(input())
years_has_to_live = int(input())
start_years = 18
for years in range(1800, years_has_to_live + 1):
    if years % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + 50 * (start_years)
    start_years += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")