# BOJ 24480, 알고리즘 수업 - 깊이 우선 탐색 2

- RANK : Silver
- Language : Python
- [알고리즘 수업](https://www.acmicpc.net/problem/24480)

<br/>

# 문제 설명

- n개의 정점과 m개의 간선으로 구성된 무방향 그래프가 주어진다. 정점 r에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문순서를 출력하라.

- i번째 줄에 정점 i의 방문 순서를 출력하여라. 시작 정점의 방문순서는 1이고 시작정점으로 부터 방문할 수 없는 경우 0을 출력한다.

<br/>

# DFS(깊이 우선 탐색)

- 재귀로 구현
- visited는 함수 밖에서 선언하고 parameter로 넘겨준다.
- 내림차순으로 방문하기 위해 edges 배열을 역순으로 정렬하였다.
- RuntimeError 때문에 recursion depth limit를 높여주여야 한다.
