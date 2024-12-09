function find(parents, target) {
  if (parents[target] !== target) {
    parents[target] = find(parents, parents[target]);
  }
  return parents[target];
}

function union(parents, a, b) {
  const pa = find(parents, a);
  const pb = find(parents, b);

  if (pa < pb) {
    parents[pb] = pa;
  } else {
    parents[pa] = pb;
  }
}

function solution(n, costs) {
  // 비용 기준으로 정렬(오름차순)
  costs.sort((a, b) => a[2] - b[2]);
  const parents = Array.from({ length: n }, (_, i) => i);

  let answer = 0; // 최소 스패닝 트리를 구성하는 간선의 가중치의 합
  for (const [a, b, c] of costs) {
    // 사이클을 생성하지 않으면 최소 스패닝 트리에 추가
    if (find(parents, a) !== find(parents, b)) {
      union(parents, a, b);
      answer += c;
    }
  }

  return answer;
}
