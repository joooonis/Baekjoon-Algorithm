function solution(targets) {
  targets.sort((a, b) => a[0] - b[0]);
  let tail = -1;
  let answer = 0;
  targets.forEach(([s, e]) => {
    if (tail <= s) {
      tail = e;
      answer++;
    } else if (e < tail) {
      tail = e;
    }
  });

  return answer;
}
