def calculations(operatior, num_one, num_two):
    if operatior == "multiply":
        return num_one * num_two
    elif operatior == "divide":
        return num_one // num_two
    elif operatior == "subtract":
        return num_one - num_two
    elif operatior == "add":
        return num_one + num_two


operator = input()
number_one = int(input())
number_two = int(input())
result = calculations(operator,number_one,number_two)
print(result)