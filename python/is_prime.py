from math import sqrt, ceil

def is_prime(n):
    if n == 1:
        return "Not prime"
    elif n == 2:
        return "Prime"
    else:
        for i in range(2, ceil(sqrt(n))+1):
            if n % i == 0:
                return "Not prime"
    return "Prime"


print(is_prime(71))
