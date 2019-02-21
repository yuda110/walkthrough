
def gap_insertion_sort(target, interval, start):
    # the 'nth' element in sublist is alist[start + gap*n]
    for index in range(start, len(target), interval):
        position = index
        currentValue = target[index]
        while position >= interval and target[position-interval] > currentValue:
            target[position] = target[position - interval]
            position -= interval
        target[position] = currentValue

def shell_sort(target):
    interval = len(target) // 2
    while interval > 0:
        for i in range(interval):
            gap_insertion_sort(target, interval, i)
        interval = interval // 2
    return target


if __name__ == '__main__':
    target = [53, 23, 1, 8, 99, 341, 2, 0, 4]
    result = shell_sort(target)
    print(result)
