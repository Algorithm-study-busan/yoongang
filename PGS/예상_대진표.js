function solution(n, a, b) {
  let answer = 0;
  let A = a;
  let B = b;
  while (1) {
    answer++;
    A = Math.ceil(A / 2);
    B = Math.ceil(B / 2);
    if (A === B) return answer;
  }
}
