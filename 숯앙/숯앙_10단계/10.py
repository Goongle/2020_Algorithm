# #1 소수  8 1 2 4 8
# count_Num = int(input())
# num_List = list(map(int, input().split()))

# count = 0
# for i in range(count_Num):
#     div_Count = 0
#     for j in range(num_List[i]):
#         if num_List[i] % (j + 1) == 0:
#             div_Count += 1
        
#     if div_Count == 2:
#         count += 1
# print(count)

#2
# import sys
# M = int(sys.stdin.readline()) # M 이상
# N = int(sys.stdin.readline()) # N 이하

# num_List = [num for num in range(M, N + 1)]
# result_List = []

# for i in num_List:
#     div_Count = 0
#     for j in range(i):
#         if i % (j + 1) == 0:
#             div_Count += 1
#         if div_Count > 2:
#             break
    
#     if div_Count == 2:
#         result_List.append(i)

# if not result_List:
#     print(-1)
# else:
#     print(sum(result_List), min(result_List), sep = '\n')

#3
# import sys
# import math
# M, N = map(int, sys.stdin.readline().split()) # M 이상 N 이하
# num_List = [num for num in range(M, N + 1)]
# result_List = []

# for i in num_List:
#     div_Count = 0
#     for j in range(i):
#         if i % (j + 1) == 0:
#             div_Count += 1
#         if div_Count > 2:
#             break
    
#     if div_Count == 2:
#         sys.stdout.write(str(i) + '\n')

#3
# import math
# def is_Prime(num):
#     if(num == 1):
#         return False
#     n = int(math.sqrt(num)) + 1       
#     for i in range(2, n):
#         if num % i == 0:
#             return False
#     return True
          
# M, N = map(int, input().split())

# for i in range(M, N + 1):
#     if is_Prime(i):
#         print(i)

#4
# import math
# import sys
# def is_Prime(num):
#     if(num == 1):
#         return False
#     n = int(math.sqrt(num)) + 1
#     for i in range(2, n):
#         if num % i == 0:
#             return False
#     return True

# while(True):
#     count = 0
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break

#     for i in range(n + 1, (2 * n) + 1):
#         if is_Prime(i):
#             count += 1
#     print(count)

#5
# import math
# import sys
# def is_Prime(num):
#     if(num == 1):
#         return False
#     n = int(math.sqrt(num)) + 1
#     for i in range(2, n):
#         if num % i == 0:
#             return False
#     return True

# test_Count = int(sys.stdin.readline())
# for i in range(test_Count):
#     num = int(sys.stdin.readline())
#     prime_List = []
#     sub_List = []

#     for i in range(1, (num // 2) + 1):
#         if is_Prime(i):
#             if is_Prime(num - i):
#                 prime_List.append(i)
#                 sub_List.append(abs(i - (num - i)))
#     result = prime_List[sub_List.index(min(sub_List))]
#     print(result, num - result)

#6
# x, y, w, h = list(map(int, input().split())) # (x, y): 현재 위치 (w, h): 목표 위치
# result = min(x, y, w - x, h - y)
# print(result)

#7
# location_x = []
# location_y = []
# for i in range(3):
#     x, y = map(int,input().split())
#     location_x.append(x)
#     location_y.append(y)
# for i in range(3):
#     if location_x.count(location_x[i]) == 1:
#         result_X = location_x[i]
#     if location_y.count(location_y[i]) == 1:
#         result_Y = location_y[i]
# print(result_X, result_Y)

#8
# import math

# num_List = []
# while True:
#     num_List = list(map(int, input().split()))
#     if sum(num_List) == 0:
#         break
#     num_List.sort()
#     if pow(num_List[2], 2) == pow(num_List[0], 2) + pow(num_List[1], 2):
#         print("right")
#     else:
#         print("wrong")

#9
# import math
# R = int(input())

# euclid = R * R * math.pi
# taxi = 2 * R * R # 2r^2

# print(round(euclid, 6), format(taxi, '.6f'), sep = '\n')

#10
import math
test_Count = int(input())
for i in range(test_Count):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) 
    D = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    if D == 0: # 중심이 같을 때
        if r1 == r2: # 같은 원일 때
            print(-1)
        else: # 만나지 않을 때
            print(0)
    else:
        if D == (r1 + r2) or D == abs(r1 - r2) : ### 원이 한 점에서 만날 때
            print(1)
        elif D < (r1 + r2) and D > abs(r1 - r2) : ### 원이 두 점에서 만날 때
            print(2)
        else: # D > (r1 + r2) 원이 만나지 않을 때
            print(0)