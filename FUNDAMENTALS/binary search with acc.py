ll = [1,2,3,4,5,6,7,8]
target = 5


def index_finder(data,target, acc=0):
    head, *tail = data
    if head == target:
        return acc
    return index_finder(tail, target, acc+1)


def binary_search(data, target):
    if not data:
        return False
    if target == data[len(data)//2]:
        return index_finder(ll, target)
    elif target > data[len(data)//2]:
        return binary_search(data[len(data)//2+1:], target)
    return binary_search(data[:len(data)//2], target)


print(binary_search(ll,5))