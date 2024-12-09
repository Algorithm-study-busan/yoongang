function find(parents, target) {
  if (parents[target] !== target) {
    parents[target] = find(parents, parents[target]);
  }
  return parents[target];
}

function union(parents, a, b) {
  const pa = find(parents, a);
  const pb = find(parents, b);

  if (pa > pb) {
    parents[pa] = pb;
  } else {
    parents[pb] = pa;
  }
}

function solution(n, wires) {
  let answer = 101;
  for (let i = 0; i < wires.length; i++) {
    const parents = Array.from({ length: n + 1 }, (_, i) => i);

    for (let j = 0; j < wires.length; j++) {
      // 끊은 전선
      if (i === j) continue;

      const [a, b] = wires[j];
      // 전선이 있는 두 송전탑을 연결
      union(parents, a, b);
    }

    const count = {};
    const ps = parents.slice(1);
    for (const p of ps) {
      // 송전탑의 parents에 루트 송전탑이 아니라 부모 송전탑이 저장되는 경우도 있기 때문에
      // 루트 송전탑을 찾아서 개수 카운트
      const k = find(parents, p);
      if (k in count) {
        count[k]++;
      } else {
        count[k] = 1;
      }
    }

    const counts = Object.values(count);
    const diff = Math.abs(counts[0] - counts[1]);

    answer = Math.min(answer, diff);
  }

  return answer;
}
