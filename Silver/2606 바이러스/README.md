# BOJ 2606, 바이러스

- RANK : Silver
- Language : Python
- [바이러스](https://www.acmicpc.net/problem/2606)

<br/>

# 문제 설명

- 네트워크를 통해 전파되는 바이러스가 있다. 네트워크 상에서 연결되어 있는 컴퓨터들이 주어졌을 때 1번 컴퓨터가 바이러스에 감염되었을 때 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 구하여라.

<br/>

# graph(그래프)

- dfs를 사용하여 그래프 순회를 한다.
- stack 또는 recursion을 톻애 구현 가능하다.
