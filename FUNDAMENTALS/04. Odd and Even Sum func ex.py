def odd_and_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        elif int(i) % 2 != 0:
            odd_sum += int(i)

    print(f"Odd sum = {odd_sum}", end=", ")
    print(f"Even sum = {even_sum}")


num = input()
odd_and_even_sum(num)