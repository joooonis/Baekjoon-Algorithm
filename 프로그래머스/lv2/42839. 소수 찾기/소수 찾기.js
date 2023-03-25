function solution(numbers) {
  const arr = numbers.split('');
  const set = new Set();
  const isPrime = (n) => {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) return false;
    }
    return true;
  };
  const dfs = (n, str) => {
    if (str.length > 0) set.add(Number(str));
    if (n === arr.length) return;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === null) continue;
      const temp = arr[i];
      arr[i] = null;
      dfs(n + 1, str + temp);
      arr[i] = temp;
    }
  };
  dfs(0, '');
  let answer = 0;
  for (let num of set) {
    if (isPrime(num)) answer++;
  }
  return answer;
}
