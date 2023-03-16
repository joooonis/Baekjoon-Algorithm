function solution(board) {
  var answer = 0;
  const start = findStart(board);
  const count = bfs(board, start);

  return count ? count : -1;
}

function findStart(board) {
  const rows = board.length;
  const cols = board[0].length;
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (board[i][j] === 'R') {
        return [i, j];
      }
    }
  }
}

function bfs(matrix, start) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  const visited = Array(rows)
    .fill()
    .map(() => Array(cols).fill(false));

  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];

  const queue = [start];
  visited[start[0]][start[1]] = true;
  let count = 0;

  while (queue.length > 0) {
    const curLevelSize = queue.length;
    for (let i = 0; i < curLevelSize; i++) {
      const [x, y] = queue.shift();
      if (matrix[x][y] === 'G') {
        return count;
      }

      for (let j = 0; j < 4; j++) {
        let nx = x + dx[j];
        let ny = y + dy[j];
        if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
          while (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
            if (matrix[nx][ny] === 'D') {
              break;
            }
            nx += dx[j];
            ny += dy[j];
          }
          nx -= dx[j];
          ny -= dy[j];

          if (!visited[nx][ny]) {
            queue.push([nx, ny]);
            visited[nx][ny] = true;
          }
        }
      }
    }

    count++;
  }
  return -1;
}
