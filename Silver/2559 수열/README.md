# BOJ 2559, 수열

- RANK : Silver
- Language : Python
- [수열](https://www.acmicpc.net/problem/2559)

<br/>

# 문제 설명

- 매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때, 연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.

<br/>

### 누적 합(prefix_sum)

- 준 리스트의 구간합을 매번 구하면 O(N)의 시간이 소요된다.
- 누적합 배열을 만들어두면 O(1)에 바로바로 구할 수 있다.
- sum[i+1] = s[i] + arr[i+1]
- 부분누적합, S(i, j) = S(j+1) - S(i) 이다.
