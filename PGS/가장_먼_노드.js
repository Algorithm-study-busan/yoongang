function bfs(graph, n) {
  const q = [1];
  const dist = Array.from({ length: n + 1 }, () => 0);
  dist[1] = 1;

  while (q.length) {
    const now = q.shift();

    for (const next of graph[now]) {
      if (dist[next] === 0) {
        dist[next] = dist[now] + 1;
        q.push(next);
      }
    }
  }

  return dist;
}

function solution(n, edge) {
  const graph = Array.from({ length: n + 1 }, () => []);
  for (const [a, b] of edge) {
    graph[a].push(b);
    graph[b].push(a);
  }

  const dist = bfs(graph, n);
  const max = Math.max(...dist);

  return dist.reduce((pre, cur) => (cur === max ? pre + 1 : pre), 0);
}
