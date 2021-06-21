def palindroms(list_of_ints):
    for i in list_of_ints:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


list_of_integers = input().split(", ")
palindroms(list_of_integers)
