function solution(cap, n, deliveries, pickups) {
  let answer = 0;
  let d = 0;
  let p = 0;
  for (var i = n - 1; i >= 0; i--) {
    let cnt = 0;

    d -= deliveries[i];
    p -= pickups[i];

    while (d < 0 || p < 0) {
      d += cap;
      p += cap;
      cnt += 1;
    }

    answer += (i + 1) * 2 * cnt;
  }

  return answer;
}
