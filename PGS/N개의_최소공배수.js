// 유클리드 호제법
function gcd(n, m) {
  while (m > 0) {
    const tmp = n % m;
    n = m;
    m = tmp;
  }
  return n;
}

function lcm(n, m) {
  return (n * m) / gcd(n, m);
}

function solution(arr) {
  let answer = arr[0];
  for (let i = 1; i < arr.length; i++) {
    answer = lcm(answer, arr[i]);
  }

  return answer;
}
