function solution(n, results) {
  const graph = Array.from({ length: n + 1 }, () =>
    Array.from({ length: n + 1 }, () => false)
  );

  // s와 e의 경기 결과를 가지고 있다
  for (const [s, e] of results) {
    graph[s][e] = true;
  }

  for (let k = 1; k < n + 1; k++) {
    for (let i = 1; i < n + 1; i++) {
      for (let j = 1; j < n + 1; j++) {
        // i가 k를 이기고, k가 j를 이기면 i가 j를 이긴다
        graph[i][j] = graph[i][j] || (graph[i][k] && graph[k][j]);
      }
    }
  }

  let answer = n;
  for (let i = 1; i < n + 1; i++) {
    for (let j = 1; j < n + 1; j++) {
      // 본인은 상관없으므로 패스
      if (i === j) continue;

      // 경기 결과를 알 수 없는 경우
      if (!graph[i][j] && !graph[j][i]) {
        answer--;
        break;
      }
    }
  }

  return answer;
}
