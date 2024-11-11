// 숙련도(level)에 대해 걸리는 시간
function getTime(diffs, times, level) {
  return diffs.reduce((pre, cur, index) => {
    const cnt = level - cur;
    const time_cur = times[index];
    const time_prev = times[index - 1];
    if (cnt >= 0) return pre + time_cur;

    return pre + (-1 * cnt * (time_cur + time_prev) + time_cur);
  }, 0);
}

// 최댓값 찾기
function getMax(arr) {
  let max = -Infinity;
  arr.forEach((num) => {
    if (num > max) max = num;
  });
  return max;
}

function solution(diffs, times, limit) {
  let start = 1;
  let end = getMax(diffs);

  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    const result = getTime(diffs, times, mid);

    if (result > limit) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return start;
}
