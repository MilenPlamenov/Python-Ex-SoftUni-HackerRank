def nick_validator(nickname):
    nick_is_valid = True

    if not nickname.isalnum():
        print("Nickname must consist only of letters and numbers!")
        nick_is_valid = False

    if len(nickname) < 5:
        print("Nickname is too short!")
        nick_is_valid = False
    if len(nickname) > 9:
        print("Nickname is too long!")
        nick_is_valid = False

    if nick_is_valid:
        return "--> Congratulations, the desired nickname is valid! <--"
    else:
        return "Unfortunately the desired nickname is not valid!"


def password_validator(password):
    password_is_valid = True
    count_capitals = 0
    count_digits = 0
    count_symbols = 0
    for el in password:
        if el.isdigit():
            count_digits += 1
        if el.isupper():
            count_capitals += 1
        if not el.isalnum():
            count_symbols += 1
    if count_capitals < 3:
        print("Add at least 2 capitals to your password!")
        password_is_valid = False
    if count_digits < 3:
        print("Add at least 3 numbers to your password!")
        password_is_valid = False
    if count_symbols < 2:
        print("Add at least 2 non numbers or letters to your password!")
        password_is_valid = False
    if len(password) < 6:
        print("Add at least 6 symbols to your password!")
        password_is_valid = False
    if password_is_valid:
        return "You got safety password!"
    else:
        return "Invalid password, please add new one !"


nickname_input= input("Add your desired nickname -> ")
password_input = input("Add safety password for your account -> ")
result_nick = nick_validator(nickname_input)
result_pass = password_validator(password_input)
print(result_nick)
print(result_pass)