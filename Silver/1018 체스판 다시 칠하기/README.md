# BOJ 1072, 게임

- RANK : Silver
- Language : Python
- [게임](https://www.acmicpc.net/problem/1072)

<br/>

# 문제 설명

- 게임 횟수 X와 이긴 게임 Y가 주어진다. 이때 승률값을 Z(%)(소수점 이하는 버린다)라고 할때 이후 게임 부터는 승리만 한다고 가정할 때 Z가 변하기 위한 최소 게임횟수 n번을 구하여라.

<br/>

# Binaray Search(이분탐색)

- 순서대로 찾을 경우 O(N), Binary Search의 경우 log(N)으로 소요시간을 대폭 줄일 수 있다.

1. left: 1, right: 1,000,000,000 (주어진 X의 범위의 상한) 값을 정한다
2. mid = (left + right) / 2
3. 탐색조건에 따라서 left = mid + 1 or right = mid 로 탐색범위를 줄여나가면서 원하는 값을 찾는다.
