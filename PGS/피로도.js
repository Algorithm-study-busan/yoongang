function solution(k, dungeons) {
  const results = [];

  const visited = new Array(dungeons.length).fill(false);
  dfs(dungeons, visited, results, k, 0);

  return Math.max(...results);
}

/*
 * dungeons: 모든 dungeons
 * visited: dungeon 탐험 여부
 * results: 피로도를 다 썼을 때 탐험한 dungeon의 개수 저장
 * k: 피로도
 * count: 현재 탐험한 dungeon의 개수
 */
function dfs(dungeons, visited, results, k, count) {
  // dungeons 전체를 순회하며 탐험 가능한 dungeon 찾기
  for (let i = 0; i < dungeons.length; i++) {
    if (!visited[i] && k >= dungeons[i][0]) {
      // 아직 탐함하지 않았고, 최소 필요 피로도 조건을 만족한다면 탐험
      visited[i] = true; // 탐험했기 때문에 visited 업데이트

      // i번째 dungeon을 탐험한 상태로 다음 탐험 가능한 dungeon 찾기
      dfs(dungeons, visited, results, k - dungeons[i][1], count + 1);

      // 이전에 탐험한 dungeon을 탐험하지 않은 상태로 복구
      // 즉, i번째 dungeon을 탐험하기 전 상태로 복구 후 반복문을 통해 i + 1번째 dungeon 탐험
      visited[i] = false;
    }
  }
  results.push(count);
}
