# BOJ 1037, 약수

- RANK : Bronze
- Language : Python
- [약수](https://www.acmicpc.net/problem/1037)

# 문제 설명

N의 약수(1, N 제외)가 주어졌을 때 N을 구하여랴

# 풀이

- 주어진 약수 배열을 정렬합니다.
- 약수의 개수가 짝수 : 첫항과 끝항을 곱한다.
- 약수의 개수가 홀수 : 제곱수이므로 가운데항의 제곱.
