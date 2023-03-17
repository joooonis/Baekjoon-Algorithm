function solution(numbers) {
  let answer = [];
  numbers.forEach((num) => {
    binary = num.toString(2);
    while (!isHeightNumber(binary.length)) {
      binary = '0' + binary;
    }
    answer.push(wow(binary));
  });

  return answer;
}

function wow(binary) {
  if (binary.length === 1) {
    return 1;
  }

  let mid = binary[Math.floor(binary.length / 2)];
  let left = binary.slice(0, Math.floor(binary.length / 2));
  let right = binary.slice(Math.floor(binary.length / 2) + 1, binary.length);

  if (mid === '1') {
    return wow(left) * wow(right);
  } else {
    return left.includes(1) || right.includes(1) ? 0 : 1;
  }
}

// return if the number is 2**n - 1
function isHeightNumber(n) {
  if (n === 1) return true;
  if (n % 2 === 0) return false;
  return isHeightNumber(Math.floor(n / 2));
}
