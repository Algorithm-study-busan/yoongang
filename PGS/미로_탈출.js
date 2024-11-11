function bfs(start, end, maps, n, m) {
  let count = [...new Array(n)].map(() => [...new Array(m)].map(() => 0));
  const dr = [0, 1, 0, -1];
  const dc = [1, 0, -1, 0];

  q = [];
  q.push(start);
  count[start[0]][start[1]] = 1;

  while (q.length !== 0) {
    const [r, c] = q.shift();

    for (let i = 0; i < 4; i++) {
      if (r + dr[i] >= 0 && r + dr[i] < n && c + dc[i] >= 0 && c + dc[i] < m) {
        const nr = r + dr[i];
        const nc = c + dc[i];

        if (count[nr][nc] === 0 && maps[nr][nc] !== "X") {
          count[nr][nc] = count[r][c] + 1;
          q.push([nr, nc]);
        }
      }
    }
  }

  return count[end[0]][end[1]] - 1 || -1;
}

function solution(maps) {
  const n = maps.length;
  const m = maps[0].length;

  // 시작 지점, 출구, 레버 위치
  let start, end, lever;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (maps[i][j] === "S") start = [i, j];
      else if (maps[i][j] === "E") end = [i, j];
      else if (maps[i][j] === "L") lever = [i, j];
    }
  }

  let result = 0;
  // 시작 지점 -> 레버까지의 최단거리
  let result1 = bfs(start, lever, maps, n, m);
  if (result1 === -1) return -1;
  result += result1;

  // 레버 -> 출구까지의 최단거리
  let result2 = bfs(lever, end, maps, n, m);
  if (result2 === -1) return -1;
  result += result2;

  return result;
}
