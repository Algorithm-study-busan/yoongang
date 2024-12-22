function bfs(n, graph, start) {
  const q = [start];
  const visited = Array.from({ length: n + 1 }, () => false);
  visited[start] = true;
  let count = 0;

  while (q.length) {
    const now = q.shift();

    for (const next of graph[now]) {
      if (!visited[next]) {
        visited[next] = true;
        q.push(next);
        count++;
      }
    }
  }

  return count;
}

function solution(n, results) {
  const graph = Array.from({ length: n + 1 }, () => []);
  // 승-패를 반대로 저장한 그래프
  const reverse_graph = Array.from({ length: n + 1 }, () => []);

  for (const [s, e] of results) {
    graph[s].push(e);
    reverse_graph[e].push(s);
  }

  const count = Array.from({ length: n + 1 }, () => 0);
  for (let i = 1; i < n + 1; i++) {
    // i 선수를 이기는 사람, i 선수에게 지는 사람의 수를 카운트
    count[i] = bfs(n, graph, i) + bfs(n, reverse_graph, i);
  }

  // 각 선수에 대해 (해당 선수를 이기는 사람 + 해당 선수에게 지는 사람) 개수가 n - 1이면 순위를 매길 수 있음
  return count.reduce((pre, cur) => (cur === n - 1 ? pre + 1 : pre), 0);
}
