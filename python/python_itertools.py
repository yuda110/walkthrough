from itertools import product
from itertools import combinations, combinations_with_replacement
from itertools import groupby

#itertools.product(); 요소 중복 있음
print('itertools.product()')
print(list(product('012', 'a')))		# [('0', 'a'), ('1', 'a'), ('2', 'a')]
print(list(product('012', 'a', 'b')))	# [('0', 'a', 'b'), ('1', 'a', 'b'), ('2', 'a', 'b')]


#itertools.combinations(); 요소 중복 없음
print('itertools.combinations()')
print(list(combinations(['a', 'b', 'c'], 2)))	# [('a', 'b'), ('a', 'c'), ('b', 'c')]
print(list(combinations(range(4), 2)))			# [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


#itertools.combinations_with_replacement(); 각 요소를 2번 이상 반복할 수 있음
print('itertools.combinations_with_replacement()')
print(list(combinations_with_replacement(['a', 'b', 'c'], 2)))	# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]


# itertools.groupby()
print('itertools.groupby()')
print([(a, list(b)) for a, b in groupby('aaabcccc')])	# [('a', ['a', 'a', 'a']), ('b', ['b']), ('c', ['c', 'c', 'c', 'c'])]