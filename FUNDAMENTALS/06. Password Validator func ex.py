def pass_validator(password):
    digits = 0
    is_valid = True
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    for l in password:
        if not l.isalnum():
            print("Password must consist only of letters and digits")
            is_valid = False
            break
        if l.isdigit():
            digits += 1
    if digits < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


passw = input()
pass_validator(passw)