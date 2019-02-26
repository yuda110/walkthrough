import time

# start = time.time()
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# print(sum([fibo(i) for i in range(2, 31)]))
#
# start = time.time()
# num1 = 0
# num2 = 1
# num3 = num1 + num2
# result = 0
#
# while num3 <= 4000000:
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
#     if num3 % 2 == 0:
#         result += num3
#

# start = time.time()
# def fibo(n):
#     result = 0
#     a, b = 0, 1
#     while a <= n:
#         if a % 2 == 0:
#             result += a
#         a, b = b, a+b
#     return result
#
# print(fibo(40000000000000000000))
# print(time.time() - start)

start = time.time()
def fibo(n):
    a, b = 0, 1
    while a <= n:
        if a % 2 == 0:
            yield a
        a, b = b, a + b

print(sum(list(fibo(432423524534600000000))))
print(time.time() - start)