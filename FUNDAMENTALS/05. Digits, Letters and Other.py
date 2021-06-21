symbols_digit_str = input()
letters = []
digits = []
symbols = []

for i in symbols_digit_str:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        symbols.append(i)

print("".join(digits))
print("".join(letters))
print("".join(symbols))