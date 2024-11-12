function solution(sequence) {
  const sorted = [...sequence].sort((a, b) => a - b);
  const sortedSequence = [...new Set(sorted)];

  let now = 0;
  let removed = false; // 제거된 원소가 있는지 확인
  for (const num of sequence) {
    // 순서대로 원소가 커지고 있는 경우
    if (num === sortedSequence[now]) {
      now++;
      continue;
    }

    // 원소의 순서가 올바르지 않은데 원소를 제거한적 없는 경우
    if (!removed) {
      removed = true;
      continue;
    }

    // 현재 원소가 삭제된 원소의 다음 원소인 경우
    if (num === sortedSequence[now + 1]) {
      now += 2;
      continue;
    }

    return false;
  }
  return true;
}
