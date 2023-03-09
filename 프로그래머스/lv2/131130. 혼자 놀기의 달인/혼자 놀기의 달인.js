function solution(cards) {
  let card_copy = [...cards.slice(1)];
  let groups = [];
  curr = cards[0];
  let g = [curr];
  while (card_copy.length) {
    next = cards[curr - 1];
    const idx = card_copy.indexOf(next);
    if (idx > -1) {
      card_copy.splice(idx, 1);
    }

    if (g.includes(next)) {
      groups.push(g);
      curr = card_copy.pop();
      g = [curr];
    } else {
      g.push(next);
      curr = next;
    }
  }
  if (!groups.includes(g)) {
    groups.push(g);
  }
  groups_count = groups.map((g) => g.length).sort((a, b) => b - a);
  return groups_count.length > 1 ? groups_count[0] * groups_count[1] : 0;
}
