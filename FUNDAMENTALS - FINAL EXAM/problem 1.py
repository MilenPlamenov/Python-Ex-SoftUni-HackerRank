string_input = input()

command = input()
while command != "Done":
    command = command.split(" ")
    if command[0] == "Change":
        char = command[1]
        replacement = command[2]
        string_input = string_input.replace(char, replacement)
        print(string_input)
    elif command[0] == "Includes":
        string_new = command[1]
        if string_new in string_input:
            print("True")
        else:
            print("False")
    elif command[0] == "End":
        new_string = command[1]

        if string_input.endswith(new_string):
            print("True")
        else:
            print("False")
    elif command[0] == "Uppercase":
        string_input = string_input.upper()
        print(string_input)
    elif command[0] == "FindIndex":
        char = command[1]
        index = string_input.index(char)
        print(index)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        end = index + length
        cutted_string = string_input[index:end]
        print(cutted_string)
    command = input()
