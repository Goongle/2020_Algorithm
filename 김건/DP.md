# 동적계획법 (Dynamic Programming)

## (1) 동적계획법이란?
* 전체 문제를 작은 문제로 단순화한 다음 점화식으로 만들고 재귀로 푸는 것
* [1] 전체 문제를 작은 문제로 단순화 한다. (부분 문제 정의)
* [2] 재귀적인 구조를 활용할 수 있는 점화식을 만든다.
* [3] 작은 문제를 통해 전체 문제를 해결한다.

## (2) Memoization?(메모이제이션)
* 동적계획법에서 아주 중요한 개념이라고 할 수 있다.
* 이는 함수의 값을 계산하고 계산된 값을 배열에 저장하는 방식
* 이를 통해 필요할 때마다 함수를 다시 호출하지 않고 값을 빠르게 가져올 수 있다.

## (3) 분할 정복과의 차이점?
* 분할 정복과의 차이점은 중복이 일어나는지 / 일어나지 않는지에 있다.
* [1] 분할정복 같은 경우 큰 문제 해결이 어려워 문제를 쪼개어 푸는 것이다.
* 이는 작은 문제에 대해서 반복이 일어나지 않는다.
* [2] 하지만 동적프로그래밍 같은 경우 작은 부분 문제들이 반복되는 것을 이용해 푸는 방식이다.

## (4) 동적계획법의 조건
* 작은 문제가 반복이 일어나는 경우
* 같은 문제는 구할 마다 정답이 같은 경우

## (5) 예시

### 피보나치
![image](https://user-images.githubusercontent.com/48178699/82524008-b8598500-9b68-11ea-894a-12c691478604.png)
* 예시를 들자면 피보나치 수열을 들 수 있다.
* 피보나치 수열 같은 경우 재귀로도 풀이가 가능하다. 하지만, 재귀 그림을 보면 n이 증가할수록 호출되는 함수의 크기가 늘어나므로 값을 구하기가 힘들다.
* 즉, fibonacci를 재귀함수로 풀게될 경우 지속적으로 함수를 반복하여 실행하는 것이다.
* 피보나치 문제를 보면 작은 문제들이 반복된다. (ex) f(2) = f(1) + f(0) 그리고 언제나 정답이 같다는 것을 예로 들 수 있다.
* 이를 재귀가 아닌 동적계획법으로 풀이를 구하면 다음과 같다.
![image](https://user-images.githubusercontent.com/48178699/82524013-c0192980-9b68-11ea-8415-fdea8a0c900e.png)

''' python <br>
    def fibonacci (n) :
      fibo = []
    fibo.append(1) # 0번째는 1 이므로
    fibo.append(1) # 1번째도 1 이므로
    for i in range (2, n+1) :
    fibo[n].append(fibo[n-2]+fibo[n-1]) # n-2 n-1의 합이 답이 되므로
    return fibo
'''

''' 구현 <br>
def(start_node) :
    queue = [start_node,]
    z
    while True:
        if len(queue) == 0:
            print('All node Searched')
        node = queue.pop(0) # 0번 인덱스를 pop - dequeue
        
        if node == TARGET :
            print('The target found.')
            return node
        
        children = expand(node) # node의 자식을 분해해서 children에 저장
        queue.extend(children)
   '''
