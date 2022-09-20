# BOJ 11659, 구간 합 구하기 5

- RANK : Silver
- Language : Python
- [구간 합 구하기 5](https://www.acmicpc.net/problem/11660)

<br/>

# 문제 설명

- N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오.

  <br/>

# 2차원 배열, 누적 합(prefix_sum)

- 2차원 배열에서 누적 합 배열을 구한다. n*n배열의 누적합 배열은 n+1*n+1 배열이다.
- sum[0][n] = sum[n][0] = 0
- sum[i][j] = arr[0][0] + ... + arr[i-1][j-1]
- sum[i][j] = arr[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]
- [참고한 블로그](https://yiyj1030.tistory.com/489)
