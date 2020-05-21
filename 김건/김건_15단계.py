#1
n, m = map(int, input().split()) # n 번째 수까지 출력하며 m의 길이를 가진다

check = [False] * (n + 1)
a = [0] * m


def go(index, n, m):
    if index == m:
        for i in range(m):
            print(a[i], end=' ')
        print() # 개행의 뜻
        return
    for i in range(1, n + 1):
        if check[i]:
           continue
        check[i] = True
        a[index] = i
        go(index + 1, n, m)
        check[i] = False

go(0, n, m)

#2
n, m = map(int, input().split()) # n 번째 수까지 출력하며 m의 길이를 가진다

check = [False] * (n + 1)
a = [0] * m
result = []

def go(index, n, m):
    if index == m:
        temp = []
        for i in range(m):
            temp.append(a[i])
        temp = sorted(temp)
        if temp not in result :
            result.append(temp)
        return
    for i in range(1, n + 1):
        if check[i]:
           continue
        check[i] = True
        a[index] = i
        go(index + 1, n, m)
        check[i] = False

go(0, n, m)
for temp in result :
    for i in range (0,len(temp)) :
        print(temp[i], end = " ")
    print()

  #3
  n, m = map(int, input().split()) # n 번째 수까지 출력하며 m의 길이를 가진다

check = [False] * (n + 1) # 어떤 것을 사용하는지 체크하는 것
a = [0] * m # a에 담을 값

def dsf (index,n,m) :
    if index == m :
        for i in range(m):
            print(a[i], end = " ")
        print()
        return
    for i in range (1,n+1) :
        check[i] = True
        a[index] = i
        dsf(index+1,n,m)
        check[i] = False
dsf(0,n,m)

#4
A = [0] * 8

def dfs(N, M, K, J):
    if K == M:
        string = ''
        for i in range(M):
            string += str(A[i] + 1)
            string += ' '
        print(string)
        return

    for i in range(J, N):
        A[K] = i
        dfs(N, M , K+1, i)

def _15652():
    N, M = map(int, input().split(' '))
    if M == 1:
        for i in range(1, N+1):
            print(i)
    else:
        dfs(N, M, 0, 0)

_15652()

#5
value = int(input())
result_value = 0
check1 = [False] * value # 칼럼을 가로로 하나씩 이동하므로 세로열만 확인
check2 = [False] * ((2*value)-1) # 오른쪽 아래 대각선  x -y + n -1 로 찾을 수 있음
check3 = [False] * ((2*value)-1) # 왼쪽 아래 대각선 x + y의 값으로 찾을 수 있음

def chess_check (index,n) : # 인덱스가 행을 의미하고 (X)
    global result_value
    if index == n :
        result_value = result_value + 1
        return result_value
    else :
        for j in range (0,n) : # 여기서의 j가 열을 의미 (y)
            if check1[j] == False and check2[index-j + n - 1] == False and check3[index+j] == False :
                check1[j] = True
                check2[index-j+n-1] = True
                check3[index+j] = True
                chess_check(index+1,n)
                check1[j] = False
                check2[index-j+n-1] = False
                check3[index+j] = False

chess_check(0,value)
print(result_value)

#6
ary = []
'''
ary =[[0,3, 5, 4, 6, 9, 2, 7, 8],
[7, 8, 2, 1, 0, 5, 6, 0, 9],
[0, 6, 0, 2, 7, 8, 1, 3, 5],
[3, 2, 1, 0, 4, 6, 8, 9, 7],
[8, 0, 4, 9, 1, 3, 5, 0, 6],
[5, 9, 6, 8, 2, 0, 4, 1, 3],
[9, 1, 7, 6, 5, 2, 0, 8, 0],
[6, 0, 3, 7, 0, 1, 9, 5, 2],
[2, 5, 8, 3, 9, 4, 7, 6, 0]]
'''
for i in range (0,9) :
    value1, value2, value3, value4, value5, value6, value7, value8, value9 = input().split()
    ary.append([int(value1), int(value2), int(value3), int(value4), int(value5), int(value6),int(value7), int(value8), int(value9)])
ary3 = [0] * 81 # 9개 칸의 정보 해싱해서 쓸 것
temp = 0
zero_ary = []
for i in range (0,9) :
    for j in range (0,9) :
        if ary[i][j] == 0 :
            temp = temp + 1
            zero_ary.append([i,j])
for i in range (0,9) :
    for j in range (0,9) :
        ary3[i*9+j] = ary[i][j]
def check (value,temp_x,temp_y) :
    temp_x = int(temp_x)
    temp_y = int(temp_y)
    ary1 = [False] * 10 # 가로
    ary2 = [False] * 10 # 세로
    temp_ary = [False] * 10 # check에서 둘다 0인 것 찾아내기
    for i in range (1,10) : # Check로 바꿔주기
        if ary[temp_x][(i-1)] != 0 :
            ary1[ary[temp_x][(i-1)]] = True # 숫자가 들어있으면 해당 인덱스 True로
        if ary[(i-1)][temp_y] != 0 :
            ary2[ary[(i-1)][temp_y]] = True # 숫자가 들어있으면 해당 인덱스 True로

    for i in range (1,10) :
        if ary1[i] == True or ary2[i] == True:
            temp_ary[i] = True # 가로 세로에 겹치지 않는 수 찾기
    temp_value1 = int(int((temp_x * 9 + temp_y) / 9)/3) * 3 # 행
    temp_value2 = int(int((temp_x * 9 + temp_y) % 9)/3) * 3 # 열
    for i in range (temp_value1,temp_value1 + 3):
        for j in range (temp_value2,temp_value2 + 3) :
            if ary[i][j] == 0 :
                continue
            temp_ary[ary[i][j]] = True
    for z in range (1,10) :
        if temp_ary[z] == False :
            ary[temp_x][temp_y] = z
            sudoko(value+1)
            ary[temp_x][temp_y] = 0
flag = False
def sudoko (value): # value 는 temp 의 갯수
    global flag
    if flag:
        return

    if value == temp :
        for i in range (0,9) :
            for j in range (0,9) :
                print(ary[i][j],end = " ")
            print()
        flag = True
        return
    else:
        temp_x = zero_ary[value][0] # x 인덱스 행
        temp_y = zero_ary[value][1] # y 인덱스 열
        check(value,temp_x,temp_y)
sudoko(0)

#7
value = int(input())
x = input().split()
value_ary = [] #  숫자들 들어감
op_ary = [] # + - / % 순서의 연산자 들어감
for i in range (0,value) :  # 숫자 넣음
    x[i] = int(x[i])
    value_ary.append(x[i])

total_op = 0
max_value = -1000000000 # max 값
min_value = 1000000000 #min 값
op = input().split()
for i in range (0,4) :
    temp = int(op[i])
    total_op = temp + total_op
    for j in range (0,temp) :
        if i == 0 :
            op_ary.append('+')
        elif i == 1 :
            op_ary.append('-')
        elif i == 2 :
            op_ary.append('*')
        else :
            op_ary.append('/')
            # 부호 넣어줌
op_check_ary = [False] * total_op
op_ary_index = []
def op_make (value_) : # temp_value 는 str
    global max_value
    global min_value
    temp = 0
    if value_ >= (total_op):
        for i in range (0,len(op_ary)) :
            if i == 0 :
                if op_ary[op_ary_index[i]] == '+' :
                    temp = value_ary[0] + value_ary[1]
                elif op_ary[op_ary_index[i]] == '-' :
                    temp = value_ary[0] - value_ary[1]
                elif op_ary[op_ary_index[i]] == '*' :
                    temp = value_ary[0] * value_ary[1]
                else :
                    temp = int(value_ary[0]/value_ary[1])
            else:
                if op_ary[op_ary_index[i]] == '+' :
                    temp = temp + value_ary[i+1]
                elif op_ary[op_ary_index[i]] == '-' :
                    temp = temp - value_ary[i+1]
                elif op_ary[op_ary_index[i]] == '*' :
                    temp = temp * value_ary[i+1]
                else :
                    temp = int(temp/value_ary[i+1])
        temp = int(temp)
        if int(temp) >= max_value:
            max_value = temp
        if int(temp) <= min_value:
            min_value = temp
    else:
        for i in range(0,total_op):
            if op_check_ary[i] == True:
                continue
            op_check_ary[i] = True
            op_ary_index.append(i)
            op_make(value_+1)
            op_check_ary[i] = False
            del op_ary_index [len(op_ary_index)-1]
op_make(0)
print(max_value)
print(min_value)

#8
import sys

value=int(sys.stdin.readline())
min_value  = 9999999
ary = []
for _ in range(value):
    ary.append(list(map(int, input().split())))
people_check = [False] * value
def make_team (person): # 인원 뽑은 수
    global min_value
    if person == int(value//2):
        my_team = 0
        opposite_team = 0
        temp_arys = []
        for i in range (0,len(people_check)) :
            for j in range(0,len(people_check)) :
                if people_check[i] == True and people_check[j] == True:
                    my_team = my_team + ary[i][j]
                elif people_check[i] == False and people_check[j] == False:
                    opposite_team = opposite_team + ary[i][j]
        if abs(my_team - opposite_team) < min_value :
            min_value =  abs(my_team - opposite_team)
    else :
        for num in range (1,value) :
            if people_check[num] == True :
                continue
            people_check[num] = True
            make_team(person+1)
            people_check[num] = False
people_check[0]= True
make_team(1)
print(min_value)

#8
import sys

n=int(sys.stdin.readline())

startlink=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
team=[0 for _ in range(n)]

count=0
result=9999999999999
#팀을 나누는 경우의수
#팀을 나누고 난뒤 각각의 차 구해서 최소값찾기
def maketeam(index,j):
    if index==n//2:
        global result
        global count
        start = 0#스타트팀합
        link = 0
        count+=1
        start_list=[] #담아서 비교
        link_list=[]
        for i in range(n):
            if team[i]==1:
                start_list.append(i)
            else:
                link_list.append(i)


        for i in range(len(start_list)):
            for j in range(len(start_list)):
                    start+=startlink[start_list[i]][start_list[j]]
                    link+=startlink[link_list[i]][link_list[j]]
        if start>link:
            if result>start-link:
                result=start-link
        else:
            if result>link-start:
                result=link-start
        return
        #모두 더해서 두수의 차비교
    else:
        for i in range(j,n):
            if team[i]==0:#팀정하기
                team[i]=1
                maketeam(index+1,i)
                team[i]=0
            else:
                continue

team[0]=1#1을 팀에 넣고 시작한다 반으로 줄어든다.
maketeam(1,0)
print(result)
