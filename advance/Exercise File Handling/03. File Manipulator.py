import os


def file_creator(file_name):
    with open(file_name, "w") as file:
        file.write("")


def file_add_content(file, content):
    with open(file, "w") as file:
        file.write(content+"\n")


def file_replace(file,old_string,new_string):
    try:
        with open(file, "r+") as file:
            text = "".join(file.readlines())
            replaced_content = text.replace(old_string, new_string)
            file.seek(0) #the cursor will go on pos 0
            file.write(replaced_content)
    except FileNotFoundError:
        print("An error occurred")


def file_delete(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        print("An error occurred")


command = input()
while command != "End":
    command = command.split("-")
    file_name = command[1]
    if command[0] == "Create":
        file_creator(file_name)
    elif command[0] == "Add":
        content = command[2]
        file_add_content(file_name, content)
    elif command[0] == "Replace":
        old_str = command[2]
        new_str = command[3]
        file_replace(file_name, old_str, new_str)
    elif command[0] == "Delete":
        file_delete(file_name)
    command = input()