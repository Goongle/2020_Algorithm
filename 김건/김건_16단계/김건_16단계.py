# 1번
def fibonacci (n) :
    fibo = []
    fibo.append(0) # 0번째는 1 이므로
    fibo.append(1) # 1번째도 1 이므로
    if n < 2:
        return fibo[n]
    else :
        for i in range (2, n+1) :
            temp = fibo[i-2] + fibo[i-1]
            fibo.append(temp) # n-2 n-1의 합이 답이 되므로
    return fibo[n]


value = int(input())

print(fibonacci(value))

#2번
def fibonacci (n) :
    fibo1 = [] # 0의 출력 횟수
    fibo2 = [] # 1의 출력 횟수
    fibo1.append(1) # 0번째는 1 이므로
    fibo1.append(0) # 1번째도 1 이므로
    fibo2.append(0) # 0번째는 1 이므로
    fibo2.append(1) # 1번째도 1 이므로
    if n < 2:
        return [fibo1[n],fibo2[n]]
    else :
        for i in range (2, n+1) :
            temp1 = fibo1[i-2] + fibo1[i-1]
            temp2 = fibo2[i-2] + fibo2[i-1]
            fibo1.append(temp1) # n-2 n-1의 합이 답이 되므로
            fibo2.append(temp2) # n-2 n-1의 합이 답이 되므로
        return [fibo1[n],fibo2[n]]



value = int(input())
result_ary =[]
for i in range (0,value) :
    temp = int(input())
    result_ary.append(fibonacci(temp))
for i in result_ary :
    print(str(i[0]) + " " + str(i[1]))

# 3번
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for k in range(3,n+1):
    dp[k] = (dp[k-1]+ dp[k-2])%15746
print(dp[n])

# 4번
ary =[]

ary.append(1)
ary.append(1)
ary.append(1)

for i in range (3,101) :
    ary.append(ary[i - 2] + ary[i - 3])
value = int(input()) # 총 개수 입력
result_ary = []
for i in range (0,value) :
    temp = int(input())
    result_ary.append(ary[temp-1])

for i in result_ary :
    print(i)

# 5번
value = int(input())
input_ary = [] # 모든 색의 가격을 담고 있는 배열
for i in range (0,value) :
    temp = input().split()
    temp_ary = []
    for j in range (0,3) :
        temp_ary.append(int(temp[j]))
    input_ary.append(temp_ary)

result_ary = []

temp_ary = []
temp_ary.append(input_ary[0][0])
temp_ary.append(input_ary[0][1])
temp_ary.append(input_ary[0][2])
result_ary.append(temp_ary)
del temp_ary

for i in range (1,value) :
    ary = []
    ary.append(input_ary[i][0] + min(result_ary[i-1][1],result_ary[i-1][2])) # 0 일때
    ary.append(input_ary[i][1] + min(result_ary[i-1][0],result_ary[i-1][2])) # 1 일때
    ary.append(input_ary[i][2] + min(result_ary[i-1][0],result_ary[i-1][1])) # 2 일때
    result_ary.append(ary)
print(min(result_ary[len(result_ary)-1][0],result_ary[len(result_ary)-1][1],result_ary[len(result_ary)-1][2]))


# 6번
#include <iostream>
using namespace std;

int** Sum(int** ptr, int Number)
{
	int** ptr1;
	int* Numbers;
	ptr1 = new int* [Number];

	for (int i = 0; i < Number;i++)
	{
		ptr1[i] = new int[i + 1];
	}
	for (int i = 0; i < Number; i++)
	{

		for (int j = 0; j <= i; j++)
		{
			ptr1[i][j] = 0;
		}
	}
	ptr1[0][0] = ptr[0][0];
	for (int i = 1; i < Number; i++) // 2
	{
		for (int j = 0; j < i; j++)
		{
			if (ptr1[i][j] == 0)
			{
				ptr1[i][j] = ptr1[i - 1][j] + ptr[i][j];
			}
			else
			{
				if (ptr1[i][j] < ptr1[i - 1][j] + ptr[i][j])
				{
					ptr1[i][j] = ptr1[i - 1][j] + ptr[i][j];
				}
				else
				{}
			}
			if (ptr[i][j + 1] == 0)
			{
				ptr1[i][j + 1] = ptr1[i - 1][j] + ptr[i][j + 1];
			}
			else
			{
				if (ptr1[i][j + 1] < ptr1[i - 1][j] + ptr[i][j + 1])
				{
					ptr1[i][j + 1] = ptr1[i - 1][j] + ptr[i][j + 1];
				}
				else
				{
				}
			}
		}
	}
	return ptr1;
}
int main()
{
	int Number;
	cin >> Number;

	int** ptr;

	ptr = new int* [Number];

	for (int i = 0; i < Number;i++)
	{
		ptr[i] = new int[i + 1];
	}
	for (int i = 0; i < Number; i++)
	{

		for (int j = 0; j <= i; j++)
		{

			int Number1;
			cin >> Number1;
			ptr[i][j] = Number1;
		}
	}

	int** ptr1 = Sum(ptr, Number);
	int Max = 0;
	for (int i = 0; i < Number; i++)
	{
		if (Max < ptr1[Number - 1][i])
		{
			Max = ptr1[Number - 1][i];
		}
	}
	cout << Max;
	return 0;
}
