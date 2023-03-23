function solution(begin, target, words) {
  var answer = Infinity;

  const visited = Array(words.length).fill(false);

  function dfs(current, target, count) {
    if (current === target) answer = Math.min(count, answer);
    for (let i = 0; i < words.length; i++) {
      let next = words[i];
      if (isConnect(current, next) && !visited[i]) {
        visited[i] = true;
        dfs(next, target, count + 1);
        visited[i] = false;
      }
    }
  }
    
  if (!words.includes(target)) return 0

  dfs(begin, target, 0);

  return answer ? answer : 0;
}

const isConnect = (a, b) => {
  count = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) count++;
  }
  return count === 1;
};
