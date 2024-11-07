function solution(targets) {
  targets.sort((a, b) => a[1] - b[1]);

  let now = 0; // 현재까지 검사한 구간
  let result = 0;
  for (const target of targets) {
    // 구간의 시작 지점이 now 이상(개구간이기 때문에)이면 구간 업데이트
    if (target[0] >= now) {
      result++;
      now = target[1];
    }
  }

  return result;
}
