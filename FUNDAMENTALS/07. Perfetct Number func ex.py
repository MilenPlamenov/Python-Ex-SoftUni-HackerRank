def find_perfect_num(number):
    sum_of_div = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_div += i

    if sum_of_div == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


num = int(input())
find_perfect_num(num)
