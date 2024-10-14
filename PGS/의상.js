function solution(clothes) {
  const kinds = {};
  clothes.forEach(([, kind]) => {
    if (kind in kinds) {
      kinds[kind] += 1;
    } else {
      kinds[kind] = 1;
    }
  });

  // cur + 1 : 해당 카테고리를 선택 안하는 경우
  // - 1 : 아무 의상을 선택하지 않는 경우
  return Object.values(kinds).reduce((pre, cur) => pre * (cur + 1), 1) - 1;
}
