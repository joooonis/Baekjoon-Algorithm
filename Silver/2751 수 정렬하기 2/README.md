# BOJ 2751, 수 정렬하기 2

- RANK : Bronze
- Language : Python
- [수 정렬하기 2](https://www.acmicpc.net/problem/2751)

<br />

# 문제

- O(NlogN)의 시간복잡도의 정렬 알고리즘을 사용하여야 통과된다.

  <br />

# Sorting(정렬)

- O(N^2) : bubble sort, selection sort, insertion sort
- O(NlogN) : merge sort, heap sort, qucik sort(python list.sort)
- 단 qucik sort은 쉽게 시간복잡도가 O(N^2)에 수렴할 가능성이 있다.

<br />

# Merge Sort(병합 정렬)

- Divide-and-Conquer + Recursion
- split:O(logN) + merge:O(N) = O(NlogN)
  Input : sequence S with n elements
  merge_sort(S):

1. Divide the S into two sublist

- (S1, S2) ← divide(S, n/2)

2. Recursively sort each half

- merge_sort(S1)
- merge_sort(S2)

3. Merge the two sorted sublists into a sorted list

- S ← merge(S1, S2)

  <br />

# 주의

- 입력을 받을 때 최대 백만개의 입력을 받으므로 input()이 아니라 sys.stdin.readline()로 입력을 받아야 한다.
- python list.sort가 O(NlogN)이므로 이 문제에서 역시 기본 정렬함수를 사용해도 된다.
- merge sort를 사용할 경우 Python3가 아니라 PyPy3로 제출하여야 한다.
