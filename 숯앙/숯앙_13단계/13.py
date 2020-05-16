# 1
# N, M = map(int, input().split()) # N: N장의 카드 M:목표 숫자
# num_List = list(map(int, input().split()))

# result_List =[]
# for i in range(len(num_List) - 2):
#     for j in range(i + 1, len(num_List) - 1):
#         for k in range(i + 2, len(num_List)): 
#             result = num_List[i] + num_List[j] + num_List[k]
#             if result <= M:
#                 result_List.append(result)

# print(max(result_List))

#2
# import sys
# N = int(sys.stdin.readline())
# sign = False
# for i in range(N):
#     result = i
#     i = str(i)
#     for j in range(len(i)):
#         result += int(i[j])

#     if result  == N:
#         print(i)
#         sign = True
#         break
# if not sign:
#     print(0)

#3
# import sys
# result_List = []

# N = int(sys.stdin.readline()) # N: 전체 사람의 수
# for i in range(N):
#     x, y = map(int, input().split()) # x: 몸무게 y: 키
#     temp_List = [x, y]
#     result_List.append(temp_List) # [x, y] [0, 1] 

# for i in result_List:
#     rank = 1
#     for j in result_List:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank)

#4
# def WhiteOrBlack(color, M, sign):
#     count = 0
#     for j in range(1, M):
#         #white
#         if sign % 2 == 0:
#             if j % 2 == 0:
#                 if color[j] != 'W':
#                     count += 1
#             else:
#                 if color[j] != 'B':
#                     count += 1

#         #black
#         else:
#             if j % 2 == 0:
#                 if color[j] != 'B':
#                     count += 1
#             else:
#                 if color[j] != 'W':
#                     count += 1
#     return count
# N, M = map(int, input().split()) # N: 세로, M: 가로
# count1 = 0
# count2 = 0
# for i in range(N):
#     color = input()
#     count1 += WhiteOrBlack(color, M, i)
#     count2 += WhiteOrBlack(color, M, i + 1)
#     print(count1)
#     print(count2)
# print(min(count1, count2))

#5
N = int(input())
endNum = 666

sign = True
while sign:
    if "666" in str(endNum):
        N -= 1
    endNum += 1
    if N == 0:
        sign = False

print(endNum - 1)