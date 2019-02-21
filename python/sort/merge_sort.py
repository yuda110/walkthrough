
def merge_sort(target):
    if len(target) > 1:
        mid = len(target)//2
        left = target[:mid]
        right = target[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                target[k] = left[i]
                i += 1
            else:
                target[k] = right[j]
                j += 1
            k += 1

        if i == len(left):
            while j < len(right):
                target[k] = right[j]
                j += 1
                k += 1
        elif j == len(right):
            while i < len(left):
                target[k] = left[i]
                i += 1
                k += 1

    return target


if __name__ == '__main__':
    target_list = [53, 23, 1, 8, 99, 341, 2, 0, 4]
    result = merge_sort(target_list)
    print(result)
