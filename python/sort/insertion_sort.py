
def insertion_sort(target):
    for j in range(1, len(target)):
        key = target[j]
        i = j - 1
        while i >= 0 and target[i] > key:
            target[i+1] = target[i]
            i -= 1
        target[i+1] = key
    return target


if __name__ == '__main__':
    target_list = [53, 23, 1, 8, 99, 341, 2, 0, 4]
    result = insertion_sort(target_list)
    print(result)
