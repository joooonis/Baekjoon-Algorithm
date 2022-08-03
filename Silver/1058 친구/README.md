# BOJ 1058, 친구

- RANK : Silver
- Language : Python
- [친구](https://www.acmicpc.net/problem/1058)

<br/>

# 문제 설명

- 서로 친구이거나 한다리 건너서 아는 사이일 경우 2-친구라고 한다. 2-친구가 가장 많은 사람의 2-친구 수를 구하여라.

<br/>

# 예제

### 입력

3 <br/>
NYY <br/>
YNY <br/>
YYN

### 출력

2

<br/>

# Graph

- graph의 구현방법:

  - 2차원 배열 : Adjecency Matrix,
    - A[i][j] = 1 means there's a edge
    - A[i][j] = 0 means there's no edge
  - dictionay : key=vertex, value={adjecency vertexes} 로 구현
    - ex) A = {0:{1,2,3}, 1:{0}, 2:{0,3}, 3:{0,2}}
  - Edge List Structue : Vertex List, Edge List를 만들고 edge가 vertex를 가리키게 한다.

- BFS:

  - breadth first search
  - take steps in all vertices adjacent before further taking steps
  - 시작점부터 depth에 따라 level1, level2, ... 로 구분한다.

- 본 문제의 경우 주어진 조건을 그래프로 만든 다음 BFS를 수행하여 level2 까지의 vertex 수가 2-친구의 값이다.
