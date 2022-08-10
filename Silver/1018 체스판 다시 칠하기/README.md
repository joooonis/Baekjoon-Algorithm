# BOJ 1018, 체스판 다시 칠하기

- RANK : Silver
- Language : Python
- [체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)

<br/>

# 문제 설명

주어진 MxN 크기의 보드를 잘라서 8x8 크기의 체스판으로 만들고자 한다. 보드에는 하얀색과 검은색이 규칙적이지 않게 번갈아 칠해져 있는데 체스판을 만들기위해 임의의 칸을 다시 칠을 할 수 있다. 이때 다시 칠해야 하는 칸의 최소 개수를 구해라.

<br/>

# Bruth Force

- 브루트 포스(Bruth Force)란 전수조사 즉 가능한 모든 경우를 대입하여 해답을 찾는 것을 말한다.
- python의 list comprehension을 사용하여 체스판 배열을 만들고 삼중 for문을 사용하여 주어진 보드를 잘라 체스판을 만들수 있는 모든 경우를 확인하였다.
