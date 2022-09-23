# BOJ 11286, 절댓값 힙

- RANK : Silver
- Language : Python
- [절댓값 힙](https://www.acmicpc.net/problem/11286)

<br/>

# 문제 설명

절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

1. 배열에 정수 x (x ≠ 0)를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
   프로그램은 처음에 비어있는 배열에서 시작하게 된다.

<br/>

# Heap

> python heapq

- heap을 사용하기 위해서는 heapq 모듈을 사용한다.
- from heapq import heapify, heappop
- heap = []
- heappush(heap, (우선순위, 값))
- heappop(heap)
