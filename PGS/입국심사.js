// value 시간으로 심사를 받을 수 있는 사람의 수
function count(times, value) {
  return times.reduce((pre, cur) => pre + Math.floor(value / cur), 0);
}

function solution(n, times) {
  const max = Math.max(...times);
  let start = 1;
  let end = max * n;
  while (start <= end) {
    const mid = Math.floor((start + end) / 2);

    if (count(times, mid) >= n) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return start;
}
