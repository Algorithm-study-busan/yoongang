function isPrime(n) {
  if (n <= 1) return false;

  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
}

function solution(numbers) {
  const nums = numbers.split("");
  const answer = [];

  /**
   * makeNum: 종이 조각을 사용해 만들 수 있는 모든 수를 탐색하며 소수이면 answer에 추가
   * nums: 현재 사용할 수 있는 종이 조각
   * now: 현재까지 종이 조각을 사용해 만든 수
   */
  function makeNum(nums, now) {
    for (let i = 0; i < nums.length; i++) {
      // i번째 조각을 사용할 수 있는 조각에서 삭제
      const clone = [...nums];
      clone.splice(i, 1);

      // 현재 만들어진 수 뒤에 i번째 종이 조각을 붙여서 만들어진 수
      // 0부터 시작하는 수를 제외하기 위해 parseInt 사용
      const n = parseInt(now + nums[i]);

      if (!answer.includes(n) && isPrime(n)) {
        answer.push(n);
      }
      makeNum(clone, n);
    }
  }

  makeNum(nums, "");
  return answer.length;
}
