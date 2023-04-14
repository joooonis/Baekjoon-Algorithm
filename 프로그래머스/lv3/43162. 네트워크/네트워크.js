function solution(n, computers) {
  let network = 0;
  const visited = Array(n).fill(false);

  function dfs(node) {
    visited[node] = true;
    for (let neighbor = 0; neighbor < n; neighbor++) {
      if (computers[node][neighbor] === 1 && !visited[neighbor]) dfs(neighbor);
    }
  }

  for (let node = 0; node < n; node++) {
    if (!visited[node]) {
      dfs(node);
      network++;
    }
  }
  return network;
}
