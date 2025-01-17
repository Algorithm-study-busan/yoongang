function solution(k, tangerine) {
  const count = {};
  for (const t of tangerine) {
    if (count[t]) {
      count[t]++;
    } else {
      count[t] = 1;
    }
  }

  const list = Object.values(count).sort((a, b) => b - a);
  let answer = 0;
  for (const c of list) {
    if (k < c) {
      if (k === 0) break;

      answer++;
      break;
    }

    answer++;
    k -= c;
  }

  return answer;
}
