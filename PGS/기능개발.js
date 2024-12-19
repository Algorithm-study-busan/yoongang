function solution(progresses, speeds) {
  let idx = 0;
  let day = 0;

  const answer = [];
  while (idx < progresses.length) {
    // 현재(idx번째) 기능이 배포될 수 있는데 걸리는 시간
    const period = Math.ceil(
      (100 - speeds[idx] * day - progresses[idx]) / speeds[idx]
    );
    day += period;

    // period만큼 날짜가 지나갔을 때 배포할 수 있는 기능의 개수
    let cnt = 0;
    for (let i = idx; i < progresses.length; i++) {
      if (progresses[i] + day * speeds[i] < 100) break;

      cnt++;
    }
    idx += cnt;

    answer.push(cnt);
  }

  return answer;
}
