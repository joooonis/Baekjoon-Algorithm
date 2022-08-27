# BOJ 1991, 트리 순회

- RANK : Silver
- Language : Python
- [트리 순회](https://www.acmicpc.net/problem/1991)

<br/>

# 문제 설명

- 이진트리를 입력받아 preorder traversal, inorder traversal, postorder traversal한 결과를 출력하는 프로그램을 작성하시오.

- 예제 입력 : <br/>
  7 <br/>
  A B C <br/>
  B D . <br/>
  C E F <br/>
  E . . <br/>
  F . G <br/>
  D . . <br/>
  G . . <br/>

- 예제 출력 : <br/>
  ABDCEFG <br/>
  DBAECFG <br/>
  DBEGFCA <br/>

<br/>

# Tree(binary tree, 이진트리)

- 트리를 순회하는 방법은 3종류가 있다.
- preorder : root -> leftchild -> rightchild
- inorder : leftchild -> root -> rightchild
- postorder : rightchild -> root -> leftchild
