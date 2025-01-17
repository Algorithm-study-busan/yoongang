function solution(s) {
  let cnt = 0;
  let zero = 0;

  while (s !== "1") {
    const filtered = [...s].filter((n) => {
      if (n === "0") {
        zero++;
        return false;
      }

      return true;
    });
    const len = filtered.length;

    s = len.toString(2);
    cnt++;
  }

  return [cnt, zero];
}
