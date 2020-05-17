#1
def sorting(ary) :
    for i in range (1,len(ary)) :
        for j in range (i,0,-1) :
            if ary[j] < ary[j-1]:
                ary[j],ary[j-1] = ary[j-1],ary[j]

    return ary
value = int(input())
ary = []
for i in range (0,value) :
    temp = int(input())
    ary.append(temp)
for i in range (0,len(ary)) :

    print(sorting(ary)[i])

# 삽입정렬

def sorting(ary) :
    for i in range (0,len(ary)) : # 위치를 찾는 애
        for j in range (0,len(ary)) : # 어디에 넣을까 비교 하는 애
            if ary[i]  < ary[j] :
                temp = ary[i]
                ary[i] = ary[j]
                ary[j] = temp
    return ary


value = int(input())
ary = []
for i in range (0,value) :
    temp = int(input())
    ary.append(temp)

for i in range (0,len(ary)) :
    print(sorting(ary)[i])

# 버블 정렬

#2

import sys

def merge_sorted(ary) :
    if(len(ary) >1) :
        mid = len(ary)//2
        left = ary[:mid]
        right = ary[mid:]

        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge(l,r)
    else:
        return ary

def merge(left,right) :
    i = 0
    j = 0
    ary = []
    while(i < len(left) and j < len(right)) :
        if left[i] < right[j] :
            ary.append(left[i])
            i = i + 1
        else:
            ary.append(right[j])
            j = j + 1
    while (i < len(left)) :
        ary.append(left[i])
        i = i + 1
    while (j < len(right)):
        ary.append(right[j])
        j = j + 1
    return ary

value = int(input())
ary = []
for i in range (0,value) :
    temp = int(input())
    ary.append(temp)
result = merge_sorted(ary)
for i in range (0,len(ary)) :
    print(result[i])
    # 병합정렬

#3
import sys
N = int(input())
series = [0] * 10001

for i in range(N):
    a = int(sys.stdin.readline())
    series[a] = series[a] + 1

for b in range(len(series)):
    if series[b] !=0:
        for c in range(series[b]):
            print(b)

#4
import sys
from collections import Counter
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
nums_s = Counter(nums).most_common()
print(round(sum(nums) / n))
print(nums[n // 2])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(nums[-1] - nums[0])

#5
#include <iostream>
using namespace std;


void reverse(int* ptr, int Number)
{
	for (int i = 0; i < Number; i++)
	{
		for (int j = i+1; j < Number; j++)
		{
			if (ptr[i] < ptr[j])
			{
				swap(ptr[i], ptr[j]);
			}
		}
	}
}
int main()
{

	int Number;
	int Count = 1;
	int Check = 0;
	cin >> Number;


	while (1)
	{
		if (Number % Count == Number)
		{
			break;
		}
		Count = Count * 10;
		Check++;
	}
	int* ptr = new int[Check];
	int Vertex;

	for (int i = 0;i < Check; i++)
	{
		Vertex = Number % 10;
		Number = Number / 10;
		ptr[i] = Vertex;
	}

	reverse(ptr, Check);
	for (int i = 0;i < Check; i++)
	{
		cout << ptr[i];
	}
}

#6
value = int(input())
ary = []
for i in range (0,value) :
    temp_ary = []
    temp1, temp2 = input().split()
    temp1 = int(temp1)
    temp2 = int(temp2)
    temp_ary.append(temp1)
    temp_ary.append(temp2)
    ary.append(temp_ary)
ary =sorted(ary, key = lambda x : (x[0], x[1]))
for i in ary :
    print(str(i[0]) + ' ' + str(i[1]))

#7
value = int(input())
ary = []
for i in range (0,value) :
    temp_ary = []
    temp1, temp2 = input().split()
    temp1 = int(temp1)
    temp2 = int(temp2)
    temp_ary.append(temp1)
    temp_ary.append(temp2)
    ary.append(temp_ary)
ary =sorted(ary, key = lambda x : (x[1], x[0]))
for i in ary :
    print(str(i[0]) + ' ' + str(i[1]))

#8
def sorting(ary) :
    result = []
    ary =list(set(ary))
    for i in range (0,len(ary)) :
        temp1 = len(ary[i])
        temp2 = ary[i]
        a = [temp1,temp2]
        result.append(a)
    result = sorted(result, key = lambda x : (x[0],x[1]))
    return result


value = int(input())
ary = []
for i in range (0,value) :
    temp_ary = []
    temp = input()
    ary.append(temp)
result = sorting(ary)
for i in range (0,len(result)) :
    print(result[i][1])

#9
value = int(input())
ary = []
for i in range (0,value) :
    temp1,temp2 = input().split()
    temp1 = int(temp1)
    
    ary.append([temp1,temp2])

ary = sorted(ary, key = lambda x : (x[0]))
for i in range (0,len(ary)) :
    print (str(ary[i][0]) + ' ' + ary[i][1])
