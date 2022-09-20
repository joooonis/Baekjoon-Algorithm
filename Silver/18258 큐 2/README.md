# BOJ 18258, 큐 2

- RANK : Silver
- Language : Python
- [큐 2](https://www.acmicpc.net/problem/18258)

<br/>

# 문제 설명

- 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

- push X: 정수 X를 큐에 넣는 연산이다.
- pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 큐에 들어있는 정수의 개수를 출력한다.
- empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
- front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

  <br/>

# deque(데크), python 양방향 큐

- from collections import deque
- 파이썬에서 queue를 사용할 때
- FIFO(first in fisrt out)
- 양끝 원소를 꺼내는 pop(), popleft() 연산이 O(1)로 빠르다.
- \*list의 경우 O(n)

  <br/>

# deque, method

- q = deque(): 생성자
- deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
- deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
- deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- deque.remove(item): item을 데크에서 찾아 삭제한다.
- deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).
