#1
value = int(input())
result = 0
x = input().split()
ary = []
for temp in x :
    ary.append(int(temp))

for num in ary :
    count = 0
    if num == 1 :
        continue
    for j in range (2,num) :
        if num % j == 0:
            count = count + 1
            break
    if count == 0:
        result = result + 1
print(result)


#2

value_min = int(input())
value_max = int(input())

sum = 0
min = value_max + 1
for num in range (value_min,value_max+1) :
    count = 0
    if num == 1:
        continue
    for temp_num in range (2,num) :
        if num % temp_num == 0:
            count = count + 1
            break
    if count == 0:
        sum = sum + num
        if min > num :
             min = num
if min == value_max + 1 :
    print(-1)
else :
    print(sum)
    print(min)

# 3
num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

n= num2
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

for i in range(0,len(primes)) :
    if num1 <= primes[i] :
        print(primes[i])

# 4
while(True) :
    temp_value = int(input())
    temp_value = 2 * temp_value
    if temp_value == 0:
        break
    ary = [False,False] + [True] * (temp_value - 1)
    result = []
    for indx in range (2,len(ary)) :
        if ary[indx] == True and indx > temp_value/2:
            result.append(indx)
        for j in range (2 * indx, temp_value +1, indx):
            ary[j] = False
    print(len(result))

# 5
value = int(input())

for i in range (0,value) :
    temp_value = int(input())
    ary2 = [False,False] + [True] *(temp_value - 1)
    ary = []
    for indx in range (2,len(ary2)) :
        if ary2[indx] == True:
            ary.append(indx)
        for j in range (indx *2, len(ary2),indx) :
            ary2[j] = False
    # 에라토스테네스의 체 종료
    # for 문 걸어서 true 인 것만 append 해서 작아진 배열로 하기
    result = []
    for i in range (0,len(ary)) :
        temp_result = []
        if (temp_value - ary[i]) in ary:
            temp_result.append(ary[i])
            temp_result.append(temp_value - ary[i])
            result.append(temp_result)
    min = temp_value
    min_indx = 0
    for indx in range (0,len(result)) :
        temp = abs(result[indx][0] - result[indx][1])
        if min > temp :
            min = temp
            min_indx = indx
    print(result[min_indx][0])
    print(result[min_indx][1])

#6
x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)
ary = []
ary.append(int(abs(x-w)))
ary.append(int(abs(y-h)))
ary.append(int(abs(x)))
ary.append(int(abs(y)))

min = int(abs(x-w))
for i in range (0,len(ary)) :
    if min > ary[i] :
        min = ary[i]
print(min)

#7
x1, y1 = input().split()
x2, y2 = input().split()
x3, y3 = input().split()
temp_x = 0
temp_y = 0
if x1 == x2 :
    temp_x = x3
elif x1 == x3 :
    temp_x = x2
else:
    temp_x = x1

if y1 == y2 :
    temp_y = y3
elif y1 == y3 :
    temp_y = y2
else:
    temp_y = y1

print(temp_x,temp_y)

#8
import math
while(True):
    a, b, c = input().split()
    if a == '0' and b == '0' and c == '0' :
        break
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and a > c :
        if pow(b,2) + pow(c,2) == pow(a,2) :
            print('right')
        else:
            print('wrong')
    elif b > a and b > c :
        if pow(a,2) + pow(c,2) == pow(b,2) :
            print('right')
        else:
            print('wrong')
    else :
        if pow(b,2) + pow(a,2) == pow(c,2) :
            print('right')
        else:
            print('wrong')

#9
from math import pi

r = int(input())

euclid = r*r*pi
taxi = r*r*2

print(round(euclid, 4)) # 소수점 이하 4번째 자리까지 출력
print(round(taxi, 4))

#10
n = int(input())

for i in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    R = [r1,r2,r]
    m=max(R); R.remove(m)
    print(-1 if (r==0 and r1==r2) else 1 if (r == r1+r2 or m==sum(R)) else 0 if (m > sum(R)) else 2)
