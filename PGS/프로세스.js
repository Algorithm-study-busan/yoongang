function solution(priorities, location) {
  // 순서대로 실행할 프로세스 확인용
  const sorted = [...priorities].sort((a, b) => a - b);

  let answer = 0;
  let idx = location;
  while (priorities.length) {
    answer++;
    const now = sorted.pop(); // 지금 실행될 프로세스의 우선순위
    const target = priorities.findIndex((p) => p === now);
    if (idx === target) break;

    // 프로세스를 실행한 뒤 "몇 번째로 실행되는지 알고싶은 프로세스"의 인덱스 변경
    if (idx > target) {
      idx = idx - target - 1;
    } else {
      idx = priorities.length + idx - target - 1;
    }

    // 프로세스 실행을 위해 target 앞에 있는 프로세스를 큐에서 꺼내서 다시 삽입
    for (let i = 0; i < target; i++) {
      const tmp = priorities.shift();
      priorities.push(tmp);
    }
    priorities.shift();
  }

  return answer;
}
