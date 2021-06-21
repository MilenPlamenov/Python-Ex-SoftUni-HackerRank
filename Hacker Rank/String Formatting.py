# import numbersystem
# n = int(input())
# nums = []
# for i in range(1, n + 1):
#     nums.append(i)
#     nums.append(numbersystem.decimalToOctal(i))
#     nums.append(numbersystem.decimalToHexa(i))
#     nums.append(str(numbersystem.decimalToBinary(i).lstrip("0")))
#     print(" ".join([str(i) for i in nums]))
#     nums.clear()

def bina(n):
    rep = bin(n)[2:]
    pad = m - len(rep)
    return pad * " " + rep


def inta(n):
    rep = str(n)
    pad = m - len(rep)
    return pad * " " + rep + " "


def octa(n):
    rep = oct(n)[2:]
    pad = m - len(rep)
    return pad * " " + rep + " "


def hexa(n):
    rep = hex(n)[2:].upper()
    pad = m - len(rep)
    return pad * " " + rep + " "


k = int(input())
m = len(bin(k).lstrip("0b"))

for i in range(1, k+1):
    r = [inta(i), octa(i), hexa(i), bina(i)]
    print("".join(r))