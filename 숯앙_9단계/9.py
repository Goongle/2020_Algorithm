# 1
# import sys
# A, B, C = map(int, sys.stdin.readline().split()) # A: 고정비용, B: 가변비용 C: 노트북 가격

# sign = True
# num = 0
# while (sign):
#     if B >= C:
#         print(-1)
#         sign = False
#     elif A + (B * num) < C * num:
#         print(num)
#         sign = False
#     else:
#         num += 1

# 2
# N = int(input())

# sign = True
# count = 0
# while (sign):
#     if N % 5 == 0:
#         count += (N // 5)
#         print(count)
#         sign = False
#     else:
#         N -= 3
#         count += 1
#     if N < 0:
#         print(-1)
#         sign = False

# 3
# import sys
# N = int(sys.stdin.readline()) # 37
# num = 2
# rank = 2
# count = 0

# sign = True
# while(sign): # 8
#     count += 1
#     if count == ((rank - 1) * 6):
#         num += count
#         count = 0 # 7일 때 0
#         rank += 1
#     if num > N:
#         print(rank - 1)
#         sign = False

# 4
# 1/1 1
# 1/2 2/1 2
# 3/1 2/2 1/3 3
# 1/4 2/3 3/2 4/1 4
# 5/1 4/2 3/3 2/4 1/5 5    2/4 = 14
# 1/6 2/5 3/4 4/3 5/2 6/1 6 2/5 = 17

# X = int(input())

# rank = 1
# count = 0

# sign = True
# while(sign):
#     count += rank
#     if count >= X: #X = 14 1.2 3.3. 6.4 10.5 15.6 21.
#         frac_Num = (count - X + 1)
#         if rank % 2 == 0:
#             print(f"{(rank + 1) - frac_Num}/{frac_Num}")
#             sign = False
#         else:
#             print(f"{frac_Num}/{(rank + 1) - frac_Num}")
#             sign = False
#     else:
#         rank += 1

# 5
# import sys
# A, B, V = map(int, sys.stdin.readline().split()) # A: up B: down C: distance

# if ((V - A) / (A - B)) == ((V - A) // (A - B)):
#     print(((V - A) // (A - B)) + 1)
# else:
#     print(((V - A) // (A - B)) + 2)

# 6
# # (N // H) + 1 : 뒷번호 뒷번호 길이가 1이면 앞에 0붙임
# # N % H : 앞번호 
# test_Count = int(input())
# for i in range(test_Count):
#     H, W, N = map(int, input().split()) # H: 층수 W: 방수 N: 손님 번호
#     front = N % H
#     rear = (N // H) + 1
#     if N % H == 0:
#         front = H
#         rear = N // H
#     if len(str(rear)) == 1:
#         result = str(front) + '0' + str(rear)
#     else:
#         result = str(front) + str(rear)
#     print(result)

#7
# test_Count = int(input())

# for i in range(test_Count):
#     k = int(input()) # k층
#     n = int(input()) # n호
#     people = []
#     for people_Num in range(1, n + 1):
#         people.append(people_Num)
#     for j in range(k):
#         for l in range(1, n):
#             people[l] = people[l - 1] + people[l]
    
#     print(people[n - 1])

#8
# 이전 이동거리: k, 다음 이동 거리: k-1 k k+1
# 처음 / 도착 직전의 이동거리 : 1
# 0 3 : 1 2 3
# 1 5 : 2 4 5
# 45 50 : 46 48 49 50

text_Count = int(input())
for i in range(text_Count):
    x, y = map(int, input().split()) # x: 현재 위치 y: 목표 위치
    count = 0 # 장치 작동 횟수
    num = 1 # 이동

    sign = True
    while(sign): # 1 5 : 2 4
        if count == 0:
            x += num
        else:
            if x + (num + 1) > y - 1:
                x += num
                if x > y - 1:
                    x -= 1
                    num -= 1
                    if x > y - 1:
                        x -= 1
                        num -= 1
            else:
                x += (num + 1)
                num += 1  

        count += 1
        if x == (y - 1):
            print(count + 1)
            sign = False