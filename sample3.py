from math import sqrt, ceil

def divisorSum(self, n):
    result = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            result |= {i, n // i}
    return sum(result)

target = 20
print(sum(this(target)))
