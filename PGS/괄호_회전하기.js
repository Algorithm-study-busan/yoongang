function check(str, start) {
  const stack = [];
  const dict = {
    ")": "(",
    "}": "{",
    "]": "[",
  };

  for (let i = start; i < start + str.length; i++) {
    const idx = i % str.length;
    const s = str[idx];
    if (Object.values(dict).includes(s)) {
      stack.push(s);
    } else {
      if (stack.pop() !== dict[s]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}

function solution(s) {
  let answer = 0;
  for (let i = 0; i < s.length; i++) {
    if (check(s, i)) {
      answer++;
    }
  }

  return answer;
}
