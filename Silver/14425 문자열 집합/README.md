# BOJ 14425, 문자열 집합

- RANK : Silver
- Language : Python
- [숫자카드](https://www.acmicpc.net/problem/14425)

<br/>

# 문제 설명

- N개의 문자열로 이루어진 집합 S가 주어진다. 입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

<br/>

### Binary Search(이분탐색)

- 포함되어 있는지 확인 할 때 Binary Search(이분탐색)을 사용하면 O(logN)의 시간이 들고 이를 n번 시행해도 O(nlogN)으로 상당히 빠르다.
- 정렬히 가능한 data를 사용할 때면 항상 사용할 수 있다.(문자열도 정렬가능)

### Map and Hash

- 딕셔너리를 사용할 경우 해시값을 사용하여 포함 여부를 알 수 있어서 O(1)의 시간밖에 걸리지 않는다.
