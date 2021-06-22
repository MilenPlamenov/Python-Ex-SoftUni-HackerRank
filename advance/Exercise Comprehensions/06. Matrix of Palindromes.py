rows, cols = list(map(int, input().split()))

res =[[f"{chr(num)}{chr(nn)}{chr(num)} " for nn in range(num, num +cols)] for num in range(97, 97 + rows)]
print(*[''.join(iterable) for iterable in res], sep="\n")