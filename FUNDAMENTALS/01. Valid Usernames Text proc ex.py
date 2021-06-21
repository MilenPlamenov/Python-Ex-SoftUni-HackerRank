def name_is_valid(input_name):
    allowed_chars = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"))
    if not 3 <= len(input_name) <= 16:
        return False
    if not set((input_name)).issubset(allowed_chars):
        return False
    return True


names = input().split(", ")

for name in names:
    if name_is_valid(name):
        print(name)