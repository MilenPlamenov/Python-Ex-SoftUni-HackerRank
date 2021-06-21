import random

password_length = int(input("Ënter your password length: "))

pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?QWERTYUIOPASDFGHJKLZXCVBNM"

pass_result = "".join(random.sample(pass_data, password_length))

print(pass_result)