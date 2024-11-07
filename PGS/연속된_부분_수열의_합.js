function solution(sequence, k) {
  const len = sequence.length;
  const results = [];
  
  let start = 0;
  let end = 0;
  let sum = sequence[0];
  
  while (end < len) {
      if (sum < k) {
          end++;
          sum += sequence[end];
      } else if (sum > k) {
          sum -= sequence[start];
          start++;
      } else {
          results.push([start, end]);
          end++;
          sum += sequence[end];
      }
  }
  results.sort(compare);
  
  return results[0];
}

// 1. 부분 수열의 길이로 정렬
// 2. 길이가 같다면 첫 번째 인덱스가 작은 순서로 정렬
function compare(a, b) {
  const dist = (a[1] - a[0]) - (b[1] - b[0]);
      
  if (dist === 0) return a[0] - b[0];
  return dist;
}