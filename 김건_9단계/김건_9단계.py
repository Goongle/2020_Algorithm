#1

import math

a, b, c = input().split()

a = int(a) # 고정 가격
b = int(b) # 유동가격
c = int(c) # 노트북 한대당 가격

# a <= x(c-b) 이것을 구해야함
# a +bx <= cx
# (c-b)x - a = 0
if c <= b:
    print(-1)
elif c == 0 :
    print(-1)
else:
    temp = math.trunc(a / (c-b)) + 1
    print(temp)

#2

value = int(input())
ary = []

for temp in range(0,1668) :

    if(3 * temp > value) :
        break
    if ((value- 3 * temp) % 5 == 0) :
        result =  int((value- 3 * temp)/5)
        temp_result = result + temp
        ary.append(temp_result)

if(len(ary) == 0) :
    print(-1)
else:
    result = ary[0]
    for num in ary :
        if (num < result) :
            result = num
    print(result)

#3

import math
temp = int(input())
# 3n^2 - 2n + 1 기본식
a = 3
b = -3
c = 2 - temp
if temp == 1:
    print(1)
else :
    value = int((-1 * b + math.sqrt(b*b - 4*a*c)) / (2*a)) # 근의 공식대로 나온 값
    value = value +1
    print(value)

#4
import math
value = int(input())
a = 1
b = 1
c = -2 * value
root_value =  int(math.ceil(((-1 * b) + math.sqrt(b * b - 4 * a * c))/2*a)) # 여기에 속한다는 의미
sum_value = int((root_value-1) * (root_value) /2) # 이전 그룹 더하기
if root_value % 2 == 0: # 짝수인 경우
    temp = value - sum_value
    a = temp
    b = root_value - temp + 1
else : # 홀수인 경우
    temp = value - sum_value
    a = root_value - temp + 1
    b = temp
print(str(a) +  '/' + str(b))

#5

import math
up, down, height = input().split()

up = int(up)
down = int(down)
height = int(height)
if up >= height :
    print(1)
else :
    temp_result = int(math.ceil((height - up) / (up-down)))
    if (height - up) % (up-down) == 0 :
        print(temp_result + 1)
    else:
        if height - int((height - up) /(up-down)) *(up-down) + up >= 0:
            print(temp_result + 1)
        else:
            print(temp_result + 2)


#6
import math
value = int(input()) # 몇 명의 손님을 받을 것인지
ary = []
for i in range (0,value) :
    temp_ary = []
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    temp_ary.append(a)
    temp_ary.append(b)
    temp_ary.append(c)
    ary.append(temp_ary)
result_ary = []
for temp_ary in ary :
    temp_a = temp_ary[0] # 높이
    temp_b = temp_ary[1] # 너비
    temp_c = temp_ary[2] # 손님
    result1 = int(math.ceil(temp_c/temp_a)) # 몇 호 인지
    if temp_c % temp_a == 0 :
        result2 = temp_a * 100
    else :
        result2 = temp_c % temp_a * 100
    result_ary.append(result1 + result2)

for temp in result_ary :
    print(temp)
    ## 나누기를 했을 때 0이면 끝 호수 배정

# 7
value = int(input())

ary = []
result_ary = []

for indx in range (1,15) :
    ary.append(indx)
result_ary.append(ary)
for indx in range (1,15) :
    temp_ary = []
    result = 0
    for small_index in result_ary[indx - 1]:
        result = result + small_index
        temp_ary.append(result)
    result_ary.append(temp_ary)
real_ary = []
for i in range (0,value):
    floor = int(input()) # 층
    address = int(input()) # 호수
    answer_value = result_ary[floor][address-1]
    real_ary.append(answer_value)
for num in real_ary :
    print(num)

#8
#include <iostream>
#include <cmath>

using namespace std;

int main(){
	cin.tie(0);
	int t;
	cin >> t;
	
	long long x, y;

	for(int i=0; i<t; i++){
		cin >> x >> y;
		double dist = y-x; // 두 지점 사이의 거리
		double dpow = sqrt(dist); // 거리의 제곱근
		int pow = round(sqrt(dist)); // 거리의 제곱근을 반올림

		if(dpow <= pow) cout << pow * 2 - 1 << "\n";
		else cout << pow * 2 << "\n";
	}

	return 0;
}
