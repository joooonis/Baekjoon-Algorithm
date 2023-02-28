function solution(bridge_length, weight, truck_weights) {
  var time = 0;
  let queue = [];
  let sum = 0;

  while (truck_weights.length > 0 || queue.length > 0) {
    if (queue.length === bridge_length) {
      sum -= queue.shift();
    }

    if (sum + truck_weights[0] <= weight) {
      sum += truck_weights[0];
      queue.push(truck_weights.shift());
    } else {
      queue.push(0);
    }

    time++;
    if (queue.reduce((a, b) => a + b) === 0) break;
  }

  return time;
}
