file = input()

for _ in file:
    template = file.split(".")
    type = template[1]
    files = file.split("\\")
    new_file = files[-1]
    final = new_file.split(".")
    print(f"File name: {final[0]}")
    print(f"File extension: {final[1]}")
    break