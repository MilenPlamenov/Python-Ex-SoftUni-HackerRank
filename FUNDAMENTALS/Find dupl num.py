ll = [1, 1, 1, 2, 3, 4, 4, 4, 5, 6, 6, 6, 6, 7, 8, 9]
dect = {el: 0 for el in ll}
for el in ll:
    dect[el] += 1
print([el for el in dect if dect[el] >= 2])