# On the first line of the input you will receive the concealed message. After that, until the "Reveal" command is given,
# you will be receiving strings with instructions for different operations that need to be performed upon the concealed message
# in order to interpret it and reveal its true content. There are several types of instructions, split by ":|:"
#     • InsertSpace:|:{index}
#         ◦ Inserts a single empty space at the given index. The given index will always be valid.
#     • Reverse:|:{substring}
#         ◦ If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
#         ◦ If not, print "error".
#         ◦ This operation should replace only the first occurrence of the given substring if there are more than one such occurrences.
#     • ChangeAll:|:{substring}:|:{replacement}
#         ◦ Changes all occurrences of the given substring with the replacement text.

string_input = input()

command = input()
while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        string_input = string_input[0:index] + ' ' + string_input[index:]
        print(string_input)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in string_input:
            string_input = string_input.replace(substring, "", 1)
            new_str = substring[::-1]
            string_input += new_str
            print(string_input)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        string_input = string_input.replace(substring, replacement)
        print(string_input)
    command = input()

print(f"You have a new text message: {string_input}")