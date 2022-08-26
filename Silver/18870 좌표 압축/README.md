# BOJ 18870, 좌표 압축

- RANK : Silver
- Language : Python
- [좌표 압축](https://www.acmicpc.net/problem/18870)

<br/>

# 문제 설명

수직선 위의 N개의 좌표가 주어졌을 때 좌표 압축을 한 결과를 나타내어라. 좌표 압축을 한 N개의 새로운 좌표의 개수는 기존 좌표의 개수와 같다.

<br/>

# dictionary

- 파이썬 딕셔너리의 경우 해시값을 이용하여 값을 찾으므로 걸리는 시간이 O(1)이다.
- list처럼 dictionary comprehension이 가능하다.
- dic = { lst[i]:i for i in range(len(lst)) }
