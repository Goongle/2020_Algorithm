# 2
# n = int(input())

# result = input()
# result_List = []

# for i in range(n):
#     result_List.append(int(result[i]))

# print(sum(result_List))

# 3
# import string
# s = input()

# alpha_List = list(string.ascii_lowercase)
# result_List = []
# for i in range(len(alpha_List)):
#     result_List.append(-1)

# for i in range(len(s)):
#     if s[i] in alpha_List:
#         result_List[alpha_List.index(s[i])] = s.find(s[i])
    
#     else:
#         pass

    
# for i in result_List:
#     print(i, sep = ' ')

# 4
# test_Count = int(input())

# result = str()
# for i in range(test_Count):
#     num, s = input().split()
#     for j in range(len(s)):
#         result += s[j] * int(num)
#     print(result)
#     result = str()

# 5
# import string
# import sys
# text = sys.stdin.readline().upper()

# count_List = []
# for i in range(len(text)):
#     line = []
#     line.append(text[i])
#     line.append(text.count(text[i]))
#     if line in count_List:
#         pass

#     else:
#         count_List.append(line)

# m_List = []
# alpha_List = []
# for i in range(len(count_List)):
#     m_List.append(count_List[i][1])
# M = max(m_List)

# for i in range(len(count_List)):
#     if count_List[i][1] == M:
#         alpha_List.append(count_List[i][0])

# if len(alpha_List) > 1:
#     sys.stdout.write('?')

# else:
#     sys.stdout.write(alpha_List[0])

#6
# text = input()
# count = text.count(' ') + 1
# if text[0] == ' ':
#     count -= 1
#     if text[-1] == ' ':
#         count -= 1
# elif text[-1] == ' ':
#     count -= 1

# print(count)

#7
# a, b = input().split()

# reverse_A = int(a[::-1])
# reverse_B = int(b[::-1])

# print(max(reverse_A, reverse_B))

#8
# alpha_Num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# text = input()

# count = 0
# for i in range(len(text)):
#     for j in alpha_Num:
#         if text[i] in j:
#             count += alpha_Num.index(j) + 3

# print(count)

#9
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# text = input()

# count = 0 # 크로아티아 문자의 개수
# len_Text = 0 # 크로아티아 문자의 길이
# result = 0 # 결과값
# for i in croatia:
#     if i in text:
#         text_Count = 0 # 입력값 안에 있는 크로아티아 문자의 개수
#         text_Count += text.count(i)
#         count += (1 * text_Count)
#         len_Text += (len(i) * text_Count)
#         if len(i) == 3:
#             text = text.replace(i, '   ')

# result = count + (len(text) - len_Text) # count + 단일 문자의 개수
# print(result)

#10
def group_word(text):
    count = 0
    for i in text:
        if text.count(i) == 1 and i != '/':
            count += 1
            text.replace(i, '/')
        elif text.count(i) > 1 and i != '/':
            if (i * text.count(i)) in text:
                count += 1
            else:
                count = 0
                break # group word가 아니면 포문에서 나옴
        else:
            pass
    
    if count >= 1:
        return True
    else:
        return False

num = int(input())
input_Count = 0
for i in range(num):
    input_Text = input()
    if group_word(input_Text) == True:
        input_Count += 1
print(input_Count)