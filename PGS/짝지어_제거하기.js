function solution(s) {
  const stack = [];
  for (const str of s) {
    if (stack[stack.length - 1] === str) {
      stack.pop();
    } else {
      stack.push(str);
    }
  }

  return stack.length === 0 ? 1 : 0;
}
