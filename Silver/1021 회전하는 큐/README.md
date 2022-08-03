# BOJ 1021, 회전하는 큐

- RANK : Silver
- Language : Python
- [회전하는 큐](https://www.acmicpc.net/problem/1021)

<br/>

# 문제 설명

- 양방향 큐에서 원하는 원소를 꺼내기 위해서 현재 위치를 이동시킬 때 최소이동 횟수를 구하여라.

<br/>

# Circular Queue

- front : circular queue에서 현재 위치
- %(moduler) 연산을 사용해서 front를 계산합니다.
- enqueue :
  1. queue.pop(f)
  2. f = (f + 1)%N
