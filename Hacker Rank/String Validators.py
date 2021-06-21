def checker(command):
    if command:
        print("True")
    else:
        print("False")


string_input = input()

is_there_digit = [i for i in string_input if i.isdigit()]
is_alphanumeric = [i for i in string_input if i.isalnum()]
is_there_alphas = [i for i in string_input if i.isalpha()]
is_lowercase = [i for i in string_input if i.islower()]
is_uppercase = [i for i in string_input if i.isupper()]

checker(is_alphanumeric)
checker(is_there_alphas)
checker(is_there_digit)
checker(is_lowercase)
checker(is_uppercase)

