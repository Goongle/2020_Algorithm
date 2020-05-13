# def a(n):
#     if n == 1:
#         return 0
#     else:
#         return a(n - 1) + 2
# # a = 3: a(2) + 2, a(1) + 2 + 2, 0 + 2 + 2 = 4
# print(a(3))

#1
# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# N = int(input())
# print(factorial(N))

#2
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)

# n = int(input())
# print(fibonacci(n))

#3
# import sys

# num = int(input())

# def star(i, j):
#     while(i != 0):
#         if(i % 3 == 1 and j % 3 == 1):
#             sys.stdout.write(' ')
#             return None
#         # 빈칸
#         i = i // 3
#         j = j // 3
#     sys.stdout.write('*')

# for i in range(num):
#     for j in range(num):
#             star(i, j)
#     sys.stdout.write('\n')

#4
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)

n = int(input())
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)

