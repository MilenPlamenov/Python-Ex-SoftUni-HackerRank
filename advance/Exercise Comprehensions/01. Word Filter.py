words = input().split(" ")

fil_words = [word for word in words if len(word) % 2 == 0]

print("\n".join(fil_words))