# 1. BFS 및 DFS에 대한 이해
## (1) BFS
- 너비 우선 탐석: 정점과 같은 레벨에 있는 노드들을 먼저 탐색하는 방식
![image](https://user-images.githubusercontent.com/48178699/82176251-33286300-9911-11ea-98d7-bac7c0410360.png)

- 위의 그림과 같이 A - B - C - D - G - H - I - E - F - J 순으로 방문

##(2) DFS
- 깊이 우선 탐색: 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와 다른 형제들의 자식을 타고 내려가며 순회
![image](https://user-images.githubusercontent.com/48178699/82176277-44716f80-9911-11ea-912b-1f3fdeea12e0.png)
- 위의 그림과 같이 A - B - D - E - F - C - G - H - I - J 

### 큐 및 스택을 사용하는 이유에 대해
- 깊이 우선 탐색 및 너비 우선 탐색 모두 탐색 하는 경로에 대한 값들을 저장해야 한다. 즉, 이전 단계로 돌아오기 위해 자료들이 필요한데 이를 스택과 큐에 저장하여 활용할 수 있다.

### 큐와 스택의 차이점?
- 먼저 스택은 '쌓는 것' 의 의미로 Last In First Out 이다. (나중에 넣은 것을 먼저 꺼낸다.)
- 큐는 '줄을 서서 기다리다.'의 의미로 FIrst In First Out 이다. (먼저 넣은 것을 먼저 꺼낸다.)

#### DFS 구현 
![image](https://user-images.githubusercontent.com/48178699/82176352-784c9500-9911-11ea-9c3d-595e1e38cb0d.png)

- DFS의 한 단계에서는 Pop과 Expand 두 가지를 수행
* Pop : 스택의 맨 위 노드를 꺼내는 작업.
* Expand : Pop으로 노드를 지우면서 그 노드의 자식을 모두 스택에 넣는 것을 의미. 자식이 없으면 아무 것도 넣지 않음
* / 는 지워진 노드를 의미하며 1->2로 넘어가는 과정을 설명하자면, A를 Pop 하면서 Expand하는 것을 의미. 즉 A를 지우고 A의 자식을 넣는다.
* 결과적으로 스택이 비게 되면 전체 모두 탐색했다는 의미
''' 구현  <br>
def(start_node) :
     stack = [start_node,]
     while True:
         if len(stack) == 0:
         print('Clear') 
         return None
     node = stack.pop()
     
     if node == TARGET:
         print('Target found')
         return None
     children = expand(node) # 노드 지우고 자식 노드들을 넣기
     stack.extend(children) # Children을 Stack에 쌓기
    
#### BFS 구현
![image](https://user-images.githubusercontent.com/48178699/82176316-5fdc7a80-9911-11ea-9712-93194d53db9a.png)

- BFS의 한 단계에서는 Dequeue와 Expand 두 가지를 수행한다.
* Dequeue : 큐에서 맨 앞에 있는 노드를 꺼내는 것
* Expand : Dequeue로 노드를 지우면서 그 노드의 자식을 모두 큐에 넣는 것 -> 여기서는 자식을 맨 뒤로 넣음 큐니까
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
