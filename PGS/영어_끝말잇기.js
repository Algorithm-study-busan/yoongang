function solution(n, words) {
  const count = Array.from({ length: n }, () => 0);
  const dup = {};

  let now = 0;
  let start = words[0][0];
  for (const word of words) {
    count[now]++;

    if (dup[word] || start !== word[0]) {
      return [now + 1, count[now]];
    }

    start = word[word.length - 1];
    dup[word] = 1;
    now = (now + 1) % n;
  }

  return [0, 0];
}
