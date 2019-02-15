from collections import Counter


myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

print(Counter(myList))          # Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

print(Counter(myList).items())  # dict_items([(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)])

print(Counter(myList).keys())   # dict_keys([1, 2, 3, 4, 5])

print(Counter(myList).values()) # dict_values([3, 4, 4, 2, 1])