function solution(numbers) {
  numbers = numbers.map(String); // 숫자들을 문자열로 변환
  numbers.sort((a, b) =>  (b+a)*1 - (a+b)*1);

  return numbers.join('')[0] === '0' ? '0' : numbers.join('')
}

