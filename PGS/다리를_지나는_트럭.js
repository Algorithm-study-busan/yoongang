function getWeight(now) {
  return now.reduce((pre, cur) => pre + cur, 0);
}

function solution(bridge_length, weight, truck_weights) {
  // 현재 다리의 상황
  const now = Array.from({ length: bridge_length }, () => 0);
  let answer = 0;
  // 모든 트럭이 출발할 때까지 반복
  while (truck_weights.length) {
    now.shift();
    answer++;

    // 다음 트럭이 출발할 수 있으면 도로에 트럭을 추가
    if (getWeight(now) + truck_weights[0] <= weight) {
      now.push(truck_weights.shift());
    } else {
      now.push(0);
    }
  }

  // 마지막 트럭이 출발하면 반복문이 그대로 중지되기 때문에
  // 마지막 트럭이 나가는 시간을 더해준다.
  answer += bridge_length - now.reverse().findIndex((w) => w !== 0);

  return answer;
}

function solution(bridge_length, weight, truck_weights) {
  let time = 0; // 현재 시간
  const q = [[0, 0]]; // 현재 도로 위에 올라간 트럭 [트럭 무게, 나갈 시간]
  let now_weights = 0; // 현재 도로 위 트럭의 무게 합

  // 도로 위에 차가 있거나, 출발하지 않은 트럭이 있는 경우 반복
  while (q.length || truck_weights.length) {
    // 다리 위 제일 앞에 있는 트럭이 나갈 시간이면
    if (time === q[0][1]) now_weights -= q.shift()[0];

    // 다음 트럭이 출발할 수 있다면
    if (now_weights + truck_weights[0] <= weight) {
      const w = truck_weights.shift();
      now_weights += w;
      q.push([w, time + bridge_length]);
    } else {
      // 모든 트럭이 출발한 경우가 있기 때문에 q[0] 조건문으로 (도로 위에 트럭 있는지)으로 확인
      // 도로 위에 트럭이 있다면 맨앞 트럭이 나가는 시간으로 이동
      // 마지막에 time++을 해주기 때문에 -1을 미리 해주어 시간 맞추기
      if (q[0]) time = q[0][1] - 1;
    }

    time++;
  }

  return time;
}
