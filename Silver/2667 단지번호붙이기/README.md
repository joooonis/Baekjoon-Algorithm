# BOJ 2606, 바이러스

- RANK : Silver
- Language : Python
- [바이러스](https://www.acmicpc.net/problem/2606)

<br/>

# 문제 설명

- 1은 집이 있는 곳을 0은 집이 없는 곳을 나타내는 2차원 배열지도가 있다. 지도를 가지고 연결된 집의 모임인 단지를 정의하고자 한다. 단지수와 각 단지에 속하는 집의 수를 구하여라.

<br/>

# graph(그래프)

- 2차원 배열을 그래프로 표현해 순회하는 문제이다.
- graph를 DFS로 순회하면서 coneected component를 찾는다.
