# BOJ 1927, 최소 힙

- RANK : Silver
- Language : Python
- [최소 힙](https://www.acmicpc.net/problem/1927)

<br/>

# 문제 설명

- 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

<br/>

# Heap

> python heapq

- heap을 사용하기 위해서는 heapq 모듈을 사용한다.
- from heapq import heapify, heappop
- heap = []
- heappush(heap, (우선순위, 값))
- heappop(heap)

</br>

> n번째 최댓값 또는 최솟값

- from heapq import nsamllest
- from heapq import nlargest
- 주어진 리스트에서 가장 작은 또는 가장 큰 n개의 값을 담은 리스트를 반환한다. 그 결과 리스트의 마지막 값이 n번째 최댓값, 최솟값이 된다.
- nsmallest(3, [4, 1, 7, 3, 8, 5])[-1]
- nlargest(3, [4, 1, 7, 3, 8, 5])[-1]

</br>

> heapify

- 주어진 리스트를 heap으로 변환하는 것을 말한다.
- from heapq import heapify
- heapify(lst)

</br>

> heap sort, 힙 정렬

- 단순히 heap에 넣었다가 빼면 정렬이 가능하다.

  </br>

[참고한 블로그](https://www.daleseo.com/python-heapq/)
