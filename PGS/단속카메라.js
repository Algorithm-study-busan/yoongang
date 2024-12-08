function solution(routes) {
  // 차량이 고속도로에서 나간 지점으로 정렬
  routes.sort((a, b) => a[1] - b[1]);

  let answer = 0; // 카메라 개수
  let now = -30001; // 카메라 설치 위치, 첫 번째 카메라 설치를 위해 -30001로 설정
  for (const [s, e] of routes) {
    if (s > now) {
      now = e;
      answer++;
    }
  }

  return answer;
}
