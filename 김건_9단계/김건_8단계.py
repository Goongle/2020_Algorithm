
# 1번
char = input()

print(ord(char))

# 2번

index = int(input())
str_num = input()

result = 0
for index in range (0,index) :
    result = int(str_num[index]) + result

print(result)

# 3번
str_temp = input()

#chr(98) # a가 97부터 z가 122
ary =[]
for num in range(97,123) :
    temp = chr(num)
    a = str_temp.find(temp)
    print(a)

# 4번

length = int(input())

result = ""
ary = []
for num in range(0,length) :
    temp1, temp2 = input('').split()
    temp1 = int(temp1)
    for a in temp2 :
        result = result + a * temp1
    ary.append(result)
    result = ""
for temp in ary :
    temp = temp.replace(' ','')
    print(temp, sep ='\n')

# 5번
word = input()
word = word.lower()
ary = []
for i in range (0,27) :
    ary.append(0)
for temp_word in word :
    count = 0
    for num in range(97,123) :
        temp = chr(num)
        if(temp_word.find(temp) >= 0) :
            ary[num - 97] = ary[num - 97] + 1

Max = 0
max_indx = 0
for i in range(0,27) :
    if ary[i] > Max :
        Max = ary[i]
        max_indx = i

count = 0
for i in range(0,27) :
    if (Max == ary[i]) :
        count = count + 1
if (count >= 2) :
    print('?')
else :
    print(chr(max_indx+97).upper())

# 6번
sentence = input()
sentence = sentence.split()
print(len(sentence))

# 7번
a, b = input().split()
a = a[::-1]
b = b[::-1]

if a > b :
    print(a)
else :
    print(b)

# 8번
word = input()
word = word.lower() # 97 ~ 122
time = 0
for i in word :
    temp = ord(i)
    if temp >= 97 and temp <= 99 : #abc
        time = time +3
    elif temp >= 100 and temp <= 102 : #def
        time = time +4
    elif temp >= 103 and temp <= 105 : #ghi
        time = time +5
    elif temp >= 106 and temp <= 108 : #jkl
        time = time +6
    elif temp >= 109 and temp <= 111 : #mno
        time = time +7
    elif temp >= 112 and temp <= 115 : #pqrs
        time = time +8
    elif temp >= 116 and temp <= 118 : #tuv
        time = time +9
    elif temp >= 119 and temp <= 122 : #wxyz
        time = time +10

print(time)

# 9번
word = input()
count = 0
while(True):
    if 'c=' in word :
        word = word.replace('c=','0',1)
        count = count +1
    elif 'c-' in word:
        word = word.replace('c-','0',1)
        count = count +1
    elif 'dz=' in word:
        word = word.replace('dz=','0',1)
        count = count +1
    elif 'd-' in word:
        word = word.replace('d-','0',1)
        count = count +1
    elif 'lj' in word:
        word = word.replace('lj','0',1)
        count = count +1
    elif 'nj' in word:
        word = word.replace('nj','0',1)
        count = count +1
    elif 's=' in word:
        word = word.replace('s=','0',1)
        count = count +1
    elif 'z=' in word:
        word = word.replace('z=','0',1)
        count = count +1
    else:
        break
for temp in word :
    if temp != '0':
        count = count + 1
print(count)

# 10번
num = int(input())
ary = []
for i in range(0,num) :
    temp_word = input()
    ary.append(temp_word)

count = 0
check = 0
for num1 in ary:
    for indx in range (0,len(num1)):
        if(len(num1) == 1):
            break
        if (abs(indx - num1.find(num1[indx],indx+1))) >= 2:
            if(num1.find(num1[indx],indx+1)) == -1:
                continue
            check = check + 1
            break
    if check >= 1:
        check = 0
    else:
        count = count +1
print(count)
