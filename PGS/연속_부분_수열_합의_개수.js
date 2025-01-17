function solution(elements) {
  const sums = new Set();

  for (let i = 1; i <= elements.length; i++) {
    for (let j = 0; j < elements.length; j++) {
      let sum = 0;
      for (let k = j; k < i + j; k++) {
        const idx = k % elements.length;
        sum += elements[idx];
      }
      sums.add(sum);
    }
  }

  return sums.size;
}

function solution(elements) {
  // 원형으로 이어지기 때문에 반복
  // 연속하는 부분 수열의 최대 길이는 elements의 길이와 동일하기 때문에 두 번 반복으로 충분
  const nums = [...elements, ...elements];
  const sums = new Set();

  for (let i = 0; i < elements.length; i++) {
    let sum = 0;
    for (let j = 0; j < elements.length; j++) {
      sum += nums[i + j];

      // 각 인덱스(i)를 시작점으로 만들 수 있는 모든 길이의 부분 수열의 합을 sums에 추가
      // j가 늘어남에 따라 다른 길이의 부분 수열의 합이 만들어짐
      sums.add(sum);
    }
  }

  return sums.size;
}
