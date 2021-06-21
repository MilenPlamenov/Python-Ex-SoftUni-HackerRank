def chars_in_range(char_one, char_two):
    chars = []
    for i in range(ord(char_one) + 1, ord(char_two)):
        chars.append(chr(i))
    return chars


char_o = input()
char_tw = input()
result = chars_in_range(char_o, char_tw)

print(" ".join(result))
