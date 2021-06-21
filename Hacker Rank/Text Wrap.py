import textwrap


def wrap(string, max_width):
    new_str = textwrap.wrap(string, max_width)
    return "\n".join(new_str)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)