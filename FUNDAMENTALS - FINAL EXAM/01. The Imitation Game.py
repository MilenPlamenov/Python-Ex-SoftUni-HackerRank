string_input = input()
command = input()
while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        num_of_letters = int(command[1])
        string_input = string_input + string_input[:num_of_letters]
        string_input = string_input[num_of_letters:]

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        string_input = string_input[0:index] + value + string_input[index:]
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        string_input = string_input.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {string_input}")