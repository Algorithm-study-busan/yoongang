function solution(number, k) {
  const answer = []; // stack
  let count = k;

  for (let i = 0; i < number.length; i++) {
    // 제거할 수 있는 수의 개수가 남아있고, 스택의 마지막 값이 들어갈 값보다 작으면 스택의 마지막 값을 pop
    while (count > 0 && answer[answer.length - 1] < number[i]) {
      answer.pop();
      count--;
    }

    answer.push(number[i]);
  }

  // 제거할 수 있는 수의 개수가 남았지만 스택의 마지막 수보다 작아서
  // 스택에 그대로 push된 수들을 자르기 위해 slice
  return answer.slice(0, number.length - k).join("");
}
