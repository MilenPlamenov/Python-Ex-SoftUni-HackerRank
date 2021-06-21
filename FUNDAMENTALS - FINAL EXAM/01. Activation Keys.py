# The first line of the input will be your raw activation key. It will consist of letters and numbers only.
# After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations
# that need to be performed upon the raw activation key.
# There are several types of instructions, split by ">>>":
#     • Contains>>>{substring} – checks if the raw activation key contains the given substring.
#         ◦ If it does prints: "{raw activation key} contains {substring}".
#         ◦ If not, prints: "Substring not found!"
#     • Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}
#         ◦ Changes the substring between the given indices (the end index is exclusive) to upper or lower case.
#         ◦ All given indexes will be valid.
#         ◦ Prints the activation key.
#     • Slice>>>{startIndex}>>>{endIndex}
#         ◦ Deletes the characters between the start and end indices (end index is exclusive).
#         ◦ Both indices will be valid.
#         ◦ Prints the activation key.

string_input = input()

command = input()
while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        substring = command[1]
        if substring in string_input:
            print(f"{string_input} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        if command[1] == "Upper":
            text_to_be_changed = string_input[start_index:end_index].upper()
            string_input = string_input.replace(string_input[start_index:end_index], text_to_be_changed)
        elif command[1] == "Lower":
            text_to_be_changed = string_input[start_index:end_index].lower()
            string_input = string_input.replace(string_input[start_index:end_index], text_to_be_changed)
        print(string_input)
    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        text_to_be_removed = string_input[start_index:end_index]
        string_input = string_input.replace(text_to_be_removed, "")
        print(string_input)
    command = input()
print(f"Your activation key is: {string_input}")