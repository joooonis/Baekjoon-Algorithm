function solution(want, number, discount) {
  answer = 0;
  hash = {};
  for (let i = 0; i < 10; i++) {
    hash[discount[i]] = (hash[discount[i]] || 0) + 1;
  }

  if (want.filter((w, i) => hash[w] === number[i]).length === want.length)
    answer++;

  for (let i = 10; i < discount.length; i++) {
    hash[discount[i - 10]] -= 1;
    hash[discount[i]] = (hash[discount[i]] || 0) + 1;

    if (want.filter((v, i) => hash[v] === number[i]).length === want.length)
      answer++;
  }

  return answer;
}
