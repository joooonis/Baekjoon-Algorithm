function solution(p) {
  if (p.length === 0) return '';

  const a = p[0];
  const b = p[0] === '(' ? ')' : '(';

  let a_count = 1;
  let b_count = 0;
  let idx = 1;
  while (a_count !== b_count) {
    if (p[idx] === a) a_count++;
    if (p[idx] === b) b_count++;
    idx++;
  }

  let u = p.slice(0, idx);
  let v = p.slice(idx);

  if (isRightString(u)) {
    return u + solution(v);
  } else {
    let answer = '(' + solution(v) + ')';
    u = u.slice(1, u.length - 1);
    u = u
      .split('')
      .map((v) => (v === '(' ? ')' : '('))
      .join('');
    return answer + u;
  }
}

function isRightString(str) {
  let stack = [];
  let x = str.split('');
  stack.push(x.shift());
  while (x.length > 0) {
    if (stack[stack.length - 1] === '(' && x[0] === ')') {
      stack.pop();
      x.shift();
    } else {
      stack.push(x.shift());
    }
  }
  return stack.length === 0;
}
