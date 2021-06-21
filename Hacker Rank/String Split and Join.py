def split_and_join(ll):
    ll = line.split(" ")
    return "-".join(ll)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)