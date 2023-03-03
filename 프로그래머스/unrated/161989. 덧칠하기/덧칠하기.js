function solution(n, m, section) {
  var answer = 0;

  while (section.length > 0) {
    let next = section.shift();
    answer++;

    while (section.length > 0 && section[0] <= next + m - 1) {
      section.shift();
    }
  }

  return answer;
}
