# 1. BFS �� DFS�� ���� ����
## (1) BFS
- �ʺ� �켱 Ž��: ������ ���� ������ �ִ� ������ ���� Ž���ϴ� ���
![image.png](attachment:image.png)
- ���� �׸��� ���� A - B - C - D - G - H - I - E - F - J ������ �湮

##(2) DFS
- ���� �켱 Ž��: �� ����� �ڽ��� Ÿ�� ������ ��ȸ�� ��, �ٽ� ���ƿ� �ٸ� �������� �ڽ��� Ÿ�� �������� ��ȸ
![image.png](attachment:image.png)
- ���� �׸��� ���� A - B - D - E - F - C - G - H - I - J 

### ť �� ������ ����ϴ� ������ ����
- ���� �켱 Ž�� �� �ʺ� �켱 Ž�� ��� Ž�� �ϴ� ��ο� ���� ������ �����ؾ� �Ѵ�. ��, ���� �ܰ�� ���ƿ��� ���� �ڷ���� �ʿ��ѵ� �̸� ���ð� ť�� �����Ͽ� Ȱ���� �� �ִ�.

### ť�� ������ ������?
- ���� ������ '�״� ��' �� �ǹ̷� Last In First Out �̴�. (���߿� ���� ���� ���� ������.)
- ť�� '���� ���� ��ٸ���.'�� �ǹ̷� FIrst In First Out �̴�. (���� ���� ���� ���� ������.)

#### DFS ���� 
- DFS�� �� �ܰ迡���� Pop�� Expand �� ������ ����
* Pop : ������ �� �� ��带 ������ �۾�.
* Expand : Pop���� ��带 ����鼭 �� ����� �ڽ��� ��� ���ÿ� �ִ� ���� �ǹ�. �ڽ��� ������ �ƹ� �͵� ���� ����
![image.png](attachment:image.png)
* / �� ������ ��带 �ǹ��ϸ� 1->2�� �Ѿ�� ������ �������ڸ�, A�� Pop �ϸ鼭 Expand�ϴ� ���� �ǹ�. �� A�� ����� A�� �ڽ��� �ִ´�.
* ��������� ������ ��� �Ǹ� ��ü ��� Ž���ߴٴ� �ǹ�
''' ����  <br>
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
     children = expand(node) # ��� ����� �ڽ� ������ �ֱ�
     stack.extend(children) # Children�� Stack�� �ױ�
    
#### BFS ����
- BFS�� �� �ܰ迡���� Dequeue�� Expand �� ������ �����Ѵ�.
* Dequeue : ť���� �� �տ� �ִ� ��带 ������ ��
* Expand : Dequeue�� ��带 ����鼭 �� ����� �ڽ��� ��� ť�� �ִ� �� -> ���⼭�� �ڽ��� �� �ڷ� ���� ť�ϱ�
''' ���� <br>
def(start_node) :
    queue = [start_node,]
    z
    while True:
        if len(queue) == 0:
            print('All node Searched')
        node = queue.pop(0) # 0�� �ε����� pop - dequeue
        
        if node == TARGET :
            print('The target found.')
            return node
        
        children = expand(node) # node�� �ڽ��� �����ؼ� children�� ����
        queue.extend(children)