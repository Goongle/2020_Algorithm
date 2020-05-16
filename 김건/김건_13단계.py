# 1
a,b = input().split()

a = int(a)
b = int(b)
ary = []
temp = input().split()
for i in range (0,a) :
    ary.append(int(temp[i]))

middle_ary = []
for i in range(0,len(ary)-2) :
    for j in range(i+1,len(ary)-1) :
        for z in range(j+1,len(ary)):
            temp = ary[i] + ary[j] + ary[z]
            middle_ary.append(temp)
max = middle_ary[0]
indx = 0
for i in range (0,len(middle_ary)) :
    if max > abs(b - middle_ary[i]) and middle_ary[i] <= b :
        max = abs(b - middle_ary[i])
        indx = i
print(middle_ary[indx])

# 2
value = int(input())
temp_value = len(str(value))
start_value = pow(10,temp_value-1)
count = 0
result_ary = []
for i in range (0,value) :
    result = 0
    num = str(i)
    for j in num :
        result = result + int(j)
    if result + i == value :
        result_ary.append(i)
        count = count + 1
if count == 0 :
    print(0)
else :
    print(min(result_ary))

# 3
value = int(input())
ary = []
for i in range (0,value) :
    temp_array = []
    temp1, temp2 = input().split()
    temp_array.append(int(temp1))
    temp_array.append(int(temp2))
    ary.append(temp_array)
result_ary = []
for i in range (0,len(ary)) :
    temp_h = ary[i][0]
    temp_w = ary[i][1]
    count = 0
    for j in range (0,len(ary)) :
        if ary[j][0] > temp_h and ary[j][1] > temp_w :
            count = count + 1
    result_ary.append(count + 1)

for i in result_ary :
    print(i,end = ' ')

# 4
sero, garo = input().split()
sero = int(sero)
garo = int(garo)
ary = [] # 체스판 배열

for i in range (0,sero) :
    temp_str = input()
    ary.append(temp_str)

max_garo = garo - 8 # 이동할 범위
max_sero = sero - 8 # 이동할 범위
temp_garo = 0
temp_sero = 0
result_ary = []
# 맨 앞이 흰색인 경우 # 검은색인 경우
while(True) :
    # 검은색이 먼저인 경우
    count = 0
    for i in range (temp_sero, temp_sero + 8) :
        for j in range (temp_garo,temp_garo + 8) :
            if (i + j) % 2 == 0:
                if(ary[i][j] == 'W') :
                    count = count + 1
            if (i + j) % 2 == 1:
                if(ary[i][j] == 'B') :
                    count = count + 1
    result_ary.append(count)
    # 흰색이 먼저인 경우
    count = 0
    for i in range (temp_sero, temp_sero + 8) :
        for j in range (temp_garo,temp_garo + 8) :
            if (i + j) % 2 == 0:
                if(ary[i][j] == 'B') :
                    count = count + 1
            if (i + j) % 2 == 1:
                if(ary[i][j] == 'W') :
                    count = count + 1
    result_ary.append(count)

    if temp_garo != max_garo :
        temp_garo = temp_garo + 1
    else :
        temp_garo = 0
        if temp_sero != max_sero :
            temp_sero = temp_sero + 1
        else:
            break

print(min(result_ary))

# 5
value = int(input())
temp = 666
n = 0
ary = []
while(True) :
    i = str(temp)
    if '666' in i :
        ary.append(temp)
        n = n + 1
    temp = temp + 1
    if n == 10000 :
        break

ary.sort()
print(ary[value-1])
