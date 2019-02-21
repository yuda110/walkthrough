
def bubble_sort1(target):
    cnt = 0
    for i in range(len(target)-1):
        for j in range(len(target)-1):
            cnt += 1
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]

    return target, cnt


def bubble_sort2(target):
    cnt = 0
    for i in range(len(target)-1):
        for j in range(len(target)-i-1):
            cnt += 1
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]

    return target, cnt


if __name__ == '__main__':
    target_list = [53, 23, 1, 8, 99, 341, 2, 0, 4]
    result1, cnt1 = bubble_sort1(target_list)
    result2, cnt2 = bubble_sort2(target_list)
    print(result1, cnt1)
    print(result2, cnt2)
