function solution(n) {
  const dp = Array.from({ length: n + 1 }, () => 1);

  for (let i = 2; i < n + 1; i++) {
    dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
  }

  return dp[n];
}
