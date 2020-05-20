# quick sort
# devide and conquer
def quick_Sort(input_List):
    if len(input_List) <= 1:
        return input_List
    
    pivot = input_List[len(input_List) // 2] # pivot
    small_List = []
    equal_List = []
    big_List = []

    for i in input_List:
        if i < pivot:
            small_List.append(i)
        elif i > pivot:
            big_List.append(i)
        else:
            equal_List.append(i)
    return quick_Sort(small_List) + equal_List + quick_Sort(big_List)

# def quick_Sort2(input_List):
#     def sort(low, high):
#         if high <= low:
#             return
#         mid = partition(low, high)
#         sort(low, mid - 1)
#         sort(mid, high)
    
#     def partition(low, high):
#         pivot = input_List[(low + high) // 2] # list의 가운데 값을 pivot 값으로 지정
#         while low <= high: # 시작 인덱스(low)는 계속 증가, 끝 인덱스(high)는 계속 감소시킨다.
#             while input_List[low] < pivot:
#                 low += 1
#             while input_List[high] > pivot:
#                 high -= 1
#             if low <= high:
#                 input_List[low], input_List[high] = input_List[high], input_List[low]
#                 low, high = low + 1, high - 1
#         return low

#     return sort(0, len(input_List) - 1)

# merge sort
def merge_Sort(input_List):
    if len(input_List) < 2:
        return input_List
    mid = len(input_List) // 2
    low_List = merge_Sort(input_List[:mid])
    high_List = merge_Sort(input_List[mid:])

    merge_List = []
    l = 0 # low
    h = 0 # high

    while l < len(low_List) and h < len(high_List):
        if low_List[l] < high_List[h]:
            merge_List.append(low_List[l])
            l += 1
        else:
            merge_List.append(high_List[h])
            h += 1
    merge_List += low_List[l:]
    merge_List += high_List[h:]
    return merge_List

#1
# N = int(input())

# input_List = []
# for i in range(N):
#     num = int(input())
#     input_List.append(num)

# input_List.sort()
# for i in input_List:
#     print(i)

#2
# import sys
# N = int(sys.stdin.readline())
# input_List = []
# for i in range(N):
#     num = int(input())
#     input_List.append(num)

# result = sorted(input_List)
# for i in result:
#     print(i)

#3
# import sys
# N = int(sys.stdin.readline())
# num_List = [0] * 10001

# for i in range(N):
#     num_List[int(sys.stdin.readline())] += 1
# for i in range(len(num_List)):
#     if num_List[i] != 0:
#         for j in range(num_List[i]):
#             print(i)

#4
# 산술평균 중앙값 최빈값 범위
# import sys
# from collections import Counter
# N = int(sys.stdin.readline()) # odd
# num_List = []
# for i in range(N):
#     num_List.append(int(sys.stdin.readline()))

# sort_List = sorted(num_List)
# avg = round(sum(num_List) / N) # mean
# mid = sort_List[len(sort_List) // 2] # median
# num_Range = max(num_List) - min(num_List) # range = max - min
# # count_List = []
# #mode
# # for i in sort_List: # from collections import Counter // most_common()
# #     temp = [i, sort_List.count(i)]
# #     if temp not in count_List:
# #         count_List.append(temp)
# # count_List = sorted(count_List, key = lambda x : (x[1], -x[0]))

# # if len(count_List) > 1:
# #     if count_List[len(count_List) - 1][0] == count_List[len(count_List) - 2][0]:
# #         mode = count_List[len(count_List) - 1][0]
# #     else:
# #         mode = count_List[len(count_List) - 2][0]
# # else:
# #     mode = count_List[0][0]
# mode_Dict = Counter(sort_List)
# count_Dict = mode_Dict.most_common()
# if len(num_List) > 1:
#     if count_Dict[0][1] == count_Dict[1][1]:
#         mode = count_Dict[1][0]
#     else: 
#         mode = count_Dict[0][0]
# else: 
#     mode = count_Dict[0][0]

# print(avg, mid, mode, num_Range, sep = '\n')

#5
# import sys
# N = int(sys.stdin.readline())
# N = str(N)
# num_List = []
# for i in N:
#     num_List.append(int(i))
# num_List = sorted(num_List, reverse = True)
# result = str()
# for i in num_List:
#     i = str(i)
#     result += i
# print(result)

#6
# import sys
# N = int(sys.stdin.readline())
# xy_List = []
# for i in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     temp = [x, y]
#     xy_List.append(temp)
# xy_List = sorted(xy_List, key = lambda x : (x[0], x[1]))
# for i in range(len(xy_List)):
#     print(xy_List[i][0], xy_List[i][1])

#7
# import sys
# N = int(sys.stdin.readline())
# xy_List = []
# for i in range(N):
#     x, y = map(int, sys.stdin.readline().split())
#     temp = [x, y]
#     xy_List.append(temp)
# xy_List = sorted(xy_List, key = lambda x : (x[1], x[0]))
# for i in range(len(xy_List)):
#     print(xy_List[i][0], xy_List[i][1])

#8
import sys
# N = int(sys.stdin.readline())
# text_List = []
# for i in range(N):
#     text = str(input())
#     text_List.append((len(text), text))
# text_List = list(set(text_List))
# text_List = sorted(text_List, key = lambda x : (x[0], x[1]))

# for i in range(len(text_List)):
#     print(text_List[i][1])

#9
N = int(sys.stdin.readline())
text = []
for i in range(N):
    text.append(list(sys.stdin.readline().split()))
text = sorted(text, key = lambda x : int(x[0]))
for i in range(N):
    print(text[i][0], text[i][1])