
def selection_sort(target):
    for i in range(len(target)-1):
        for j in range(i+1, len(target)):
            if target[i] > target[j]:
                target[i], target[j] = target[j], target[i]
    return target


if __name__ == '__main__':
    target_list = [53, 23, 1, 8, 99, 341, 2, 0, 4]
    result = selection_sort(target_list)
    print(result)
