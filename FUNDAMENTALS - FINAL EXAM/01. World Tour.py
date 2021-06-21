# On the first line you will be given a string containing all of your stops. Until you receive the command "Travel",
# you will be given some commands to manipulate that initial string. The commands can be:
#     • Add Stop:{index}:{string} – insert the given string at that index only if the index is valid
#     • Remove Stop:{start_index}:{end_index} – remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
#     • Switch:{old_string}:{new_string} – if the old string is in the initial string, replace it with the new one. (all occurrences)
# Note: After each command print the current state of the string
# After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"


string_input = input()

command = input()
while command != "Travel":
    new_command = command.split(":")
    if new_command[0] == "Add Stop":
        index = int(new_command[1])
        string = new_command[2]
        if 0 <= index < len(string_input):
            string_input = string_input[0:index] + string + string_input[index:]
        print(string_input)
    elif new_command[0] == "Remove Stop":
        start_index = int(new_command[1])
        end_index = int(new_command[2])
        if 0 <= start_index < len(string_input) and 0 <= end_index < len(string_input):
            text_to_be_removed = string_input[start_index:end_index+1]
            string_input = string_input.replace(text_to_be_removed, "")
        print(string_input)
    elif new_command[0] == "Switch":
        old_string = new_command[1]
        new_string = new_command[2]
        if old_string in string_input:
            string_input = string_input.replace(old_string, new_string)
        print(string_input)
    command = input()

print(f"Ready for world tour! Planned stops: {string_input}")