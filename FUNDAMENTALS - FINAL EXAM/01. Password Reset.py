# Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string and afterwards, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:
#     • TakeOdd
#         ◦  Takes only the characters at odd indices and concatenates them together to
# obtain the new raw password and then prints it.
#     • Cut {index} {length}
#         ◦ Gets the substring with the given length starting from the given index from the password and removes its first occurrence of it,
#         then prints the password on the console.
#         ◦ The given index and length will always be valid.
#     • Substitute {substring} {substitute}
#         ◦ If the raw password contains the given substring, replaces all of its
# occurrences with the substitute text given and prints the result.
#         ◦ If it doesn’t, prints "Nothing to replace!"

string_input = input()

command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        new_string = ""
        for index in range(len(string_input)):
            if index % 2 != 0:
                new_string += string_input[index]
        string_input = new_string
        print(string_input)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        string_to_be_replaced = string_input[index:index+length]
        string_input = string_input.replace(string_input[index:index+length], "", 1)  # 1 is for the first occurrence
        print(string_input)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in string_input:
            string_input = string_input.replace(substring, substitute)
            print(string_input)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {string_input}")