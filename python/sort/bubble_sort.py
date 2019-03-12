import random
import time

def bubble_sort(target):
    for i in range(len(target)-1):
        for j in range(len(target)-i-1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]

    return target


if __name__ == '__main__':
    target_list = [i for i in range(1000)]
    target_list = target_list[::-1]
    start = time.time()
    result = bubble_sort(target_list)
    print(time.time() - start)
