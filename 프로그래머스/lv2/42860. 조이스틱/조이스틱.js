function solution(name) {
  const distance = {
    A: 0,
    B: 1,
    C: 2,
    D: 3,
    E: 4,
    F: 5,
    G: 6,
    H: 7,
    I: 8,
    J: 9,
    K: 10,
    L: 11,
    M: 12,
    N: 13,
    O: 12,
    P: 11,
    Q: 10,
    R: 9,
    S: 8,
    T: 7,
    U: 6,
    V: 5,
    W: 4,
    X: 3,
    Y: 2,
    Z: 1,
  };

  let upDown = 0;
  let leftRight = name.length - 1;

  for (let i = 0; i < name.length; i++) {
    const dist = distance[name[i]];
    upDown += Math.min(dist, 26 - dist);
    let nextIndex = i + 1;
    while (nextIndex < name.length && name[nextIndex] === 'A') {
      nextIndex++;
    }
    leftRight = Math.min(leftRight, i + name.length - nextIndex + Math.min(i, name.length - nextIndex));
  }

  return upDown + leftRight;
}
