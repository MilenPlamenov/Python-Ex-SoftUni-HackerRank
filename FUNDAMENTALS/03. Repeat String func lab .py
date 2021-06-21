def repeating_strings(string, multiply_int):
    return string * multiply_int


string_input = input()
times = int(input())
res = repeating_strings(string_input, times)
print(res)
