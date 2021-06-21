chat = []
command = input()
while command != "end":
    command = command.split(" ")
    if command[0] == "Chat":
        message = command[1]
        chat.append(message)
    elif command[0] == "Delete":
        message = command[1]
        if message in chat:
            chat.remove(message)
    elif command[0] == "Edit":
        message_to_edit = command[1]
        edited_version = command[2]
        if message_to_edit in chat:
            message_index = chat.index(message_to_edit)
            chat[message_index] = edited_version
    elif command[0] == "Pin":
        message = command[1]
        for i in range(len(chat)):
            if chat[i] == message:
                chat.pop(i)
                chat.append(message)

    elif command[0] == "Spam":
        command = command[1:]
        for item in command:
            chat.append(item)

    command = input()
print(*chat, sep="\n")
