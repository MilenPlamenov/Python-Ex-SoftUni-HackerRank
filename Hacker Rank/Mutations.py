#string manipulation
#1
# string = "abracadabra"
# l = list(string)
# l[5] = 'k'
# string = ''.join(l)
# print(string)
# abrackdabra
#2
# string = string[:5] + "k" + string[6:]
# print(string)
# abrackdabra

string_input = input()
index = int(input())
char = input()
string_input = string_input[:index] + char + string_input[index + 1:]
print(string_input)