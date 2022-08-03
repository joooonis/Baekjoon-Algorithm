# BOJ 1655, 가운데를 말해요

- RANK : Gold
- Language : Python
- [가운데를 말해요](https://www.acmicpc.net/problem/1655)

<br/>

# 문제 설명

- 정수가 하나씩 추가될 때마다 지금까지 추가된 정수들 중 중간값을 말해라. 짝수개라면 중간에 있는 두 수 중 작은 수를 말해라.

<br/>

# 중간값 찾기

- 두개의 heap을 가지고 중간값을 찾을 수 있습니다.
- min heap, max heap, Priority Queue

- Algorithm :
  1.  max heap의 크기는 min heap의 크기와 같거나, 1만큼 크다.
  2.  max heap의 root(최대 값)은 min heap의 root(최소 값)보다 작거나 같다.
  3.  [결과] 두 규칙을 유지해준다면 항상 최대 합 root값이 중간값이 된다.
