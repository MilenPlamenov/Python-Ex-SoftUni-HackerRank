string_input = input()

stack = []

for i in string_input:
    stack.append(i)
w = ""
while stack:
    w += stack.pop()

print(w)
