function solution(n, computers) {
  const visited = new Array(n).fill(false);
  let clusters = 0;
  function dfs(node) {
    visited[node] = true;
    for (let neighbor = 0; neighbor < n; neighbor++) {
      if (computers[node][neighbor] === 1 && !visited[neighbor]) {
        dfs(neighbor);
      }
    }
  }

  for (let node = 0; node < n; node++) {
    if (!visited[node]) {
      dfs(node);
      clusters++;
    }
  }
  return clusters;
}
