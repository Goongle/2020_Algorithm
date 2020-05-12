#1

def factorial (value) :
    if value == 0:
        return 1
    if value == 1:
        return 1
    else:
        return value * factorial(value-1)
value = int(input())
print(factorial(value))

#2

def fibonachi (value) :
    if value == 0:
        return 0
    if value == 1:
        return 1
    return fibonachi(value-2) + fibonachi(value-1)
value = int(input())
print(fibonachi(value))

#3
import sys

num = int(input())

def star(i, j):
    while(i != 0):
        # 몫이 1인 경우
        if(i % 3 == 1 and j % 3 == 1):
            sys.stdout.write(' ')
            return None
        # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
        i = i // 3
        j = j // 3
    sys.stdout.write('*')

for i in range(num):
    for j in range(num):
            star(i, j)
    sys.stdout.write('\n')


#4
def hanoi (n,from_,by_,to_,ary) :
    if (n == 1):
        ary.append((from_,to_))
    else :
        hanoi(n-1,from_,to_,by_,ary)
        ary.append((from_,to_))
        hanoi(n-1,by_,from_,to_,ary)
ary = []
value = int(input())
hanoi(value,1,2,3,ary)
print(len(ary))
for i in range (0,len(ary)) :
    print(str(ary[i][0]) + ' ' + str(ary[i][1]))
