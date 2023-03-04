function solution(weights) {
  let answer = 0;
  let hash = {};

  weights.forEach((w) => {
    if (hash[w]) answer += hash[w];
    if (hash[w * 2]) answer += hash[w * 2];
    if (hash[w / 2]) answer += hash[w / 2];
    if (hash[(w * 2) / 3]) answer += hash[(w * 2) / 3];
    if (hash[(w * 3) / 2]) answer += hash[(w * 3) / 2];
    if (hash[(w * 3) / 4]) answer += hash[(w * 3) / 4];
    if (hash[(w * 4) / 3]) answer += hash[(w * 4) / 3];

    if (!hash[w]) hash[w] = 1;
    else hash[w] += 1;
  });

  return answer;
}
