
def quick_sort(target):
    if len(target) <= 1:
        return target

    pivot = target[len(target) // 2]
    less = []
    more = []
    equal = []
    for a in target:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quick_sort(less) + equal + quick_sort(more)

# with no cache
# def partition(arr, start, end):
#     pivot = arr[start]
#     left = start + 1
#     right = end
#     done = False
#     while not done:
#         while left <= right and arr[left] <= pivot:
#             left += 1
#         while left <= right and pivot <= arr[right]:
#             right -= 1
#         if right < left:
#             done = True
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#     arr[start], arr[right] = arr[right], arr[start]
#     return right
#
#
# def quick_sort(arr, start, end):
#     if start < end:
#         pivot = partition(arr, start, end)
#         quick_sort(arr, start, pivot - 1)
#         quick_sort(arr, pivot + 1, end)
#     return arr
