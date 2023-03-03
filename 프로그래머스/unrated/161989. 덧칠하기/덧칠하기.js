function solution(n, m, section) {
  var answer = 0;

  while (section.length > 0) {
    let next = section.shift();
    answer++;

    while (section.length > 0 && section[0] <= next + m - 1) {
      section.shift();
    }

    if (section.length === 0) {
      break;
    }
    next = section.pop();
    answer++;

    while (section.length > 0 && section[section.length - 1] >= next - m + 1) {
      section.pop();
    }
  }

  return answer;
}
