function solution(s) {
  const stack = [];
  for (const p of s) {
    if (p === "(") {
      stack.push(p);
    } else {
      if (stack.length === 0) return false;

      const now = stack.pop();
      if (now === ")") return false;
    }
  }

  return stack.length === 0;
}
