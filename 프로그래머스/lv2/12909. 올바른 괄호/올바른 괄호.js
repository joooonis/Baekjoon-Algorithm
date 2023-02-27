function solution(s) {
  var answer = true;
  let stack = [];

  s.split('').forEach((v) => {
    if (v === ')' && stack[stack.length - 1] === '(') stack.pop();
    else stack.push(v);
  });

  return stack.length === 0 ? true : false;
}
