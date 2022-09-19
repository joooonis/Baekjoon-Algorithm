# BOJ 11659, 구간 합 구하기 4

- RANK : Silver
- Language : Python
- [구간 합 구하기 4](https://www.acmicpc.net/problem/11659)

<br/>

# 문제 설명

- 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

<br/>

### 누적 합(prefix_sum)

- 준 리스트의 구간합을 매번 구하면 O(N)의 시간이 소요된다.
- 누적합 배열을 만들어두면 O(1)에 바로바로 구할 수 있다.
- S(i, j) = S(j+1) - S(i) 이다.
