function solution(plans) {
  const answer = [];
  plans.sort((a, b) => convertToMinute(b[1]) - convertToMinute(a[1]));
  const stack = [];
  while (plans.length || stack.length) {
    const [name, start, playTime] = plans.pop();
    const endTime = convertToMinute(start) + parseInt(playTime);

    if (plans.length === 0) {
      answer.push(name);
      while (stack.length) {
        answer.push(stack.pop()[0]);
      }
      break;
    }

    const nextStart = convertToMinute(plans[plans.length - 1][1]);
    const leftTime = endTime - nextStart;
    if (leftTime > 0) {
      stack.push([name, leftTime]);
    } else if (leftTime === 0) {
      answer.push(name);
    } else {
      answer.push(name);
      let currentTime = endTime;
      while (stack.length) {
        const [stackName, stackLeftTime] = stack.pop();
        const availableTime = nextStart - currentTime;
        if (availableTime >= stackLeftTime) {
          answer.push(stackName);
          currentTime += stackLeftTime;
        } else {
          stack.push([stackName, stackLeftTime - availableTime]);
          break;
        }
      }
    }
  }

  return answer;
}

const convertToMinute = time => {
  const [hour, minute] = time.split(':').map(Number);
  return hour * 60 + minute;
};
