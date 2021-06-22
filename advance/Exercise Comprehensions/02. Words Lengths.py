# def words_length(words):
#     return [len(word) for word in words]
#
#
# def words_ret(words):
#     return [word for word in words]
#
#
# def print_results(words):
#     print
#
#
# words = input().split(", ")
# words_length(words)
# words_ret(words)
# print_results(words)

words = input().split(", ")
fil_w = []

for w in words:
    fil_w.append(f'{w} -> {len(w)}')

print(", ".join(fil_w))