function dist(alphabet) {
  return Math.min(alphabet.charCodeAt() - 65, 91 - alphabet.charCodeAt());
}

function solution(name) {
  let count = 0;
  let min = name.length - 1; // 그냥 오른쪽으로 쭉 이동하면서 조작한 경우

  [...name].forEach((a, i) => {
    count += dist(a); // 상/하 이동

    // 왼쪽으로 돌아갔을 때 A가 아닌 문자를 모두 탐색하기 위한 인덱스: last
    // [MONAAAJOE]이고 i = 2인 경우, last = 6이 된다.
    // 이 말은 M - O - N - O - M - E - O - J 순서로 왼쪽으로 돌아갔을 때 J까지 탐색하기 위해 J의 인덱스를 저장하는 것이다.
    // i = 1인 경우는 last = 2가 되고 반복문이 끝난 후 Math.min에서 큰 값을 가지게 되어 의미가 없다.
    let last = i + 1;
    while (last < name.length && name[last] === "A") {
      last++;
    }

    min = Math.min(
      min,
      i * 2 + (name.length - last), // 오른쪽 방향으로 갔다가 왼쪽으로 되돌아가서 탐색하는 경우
      (name.length - last) * 2 + i // 왼쪽 방향으로 갔다가 오른쪽으로 되돌아가서 탐색하는 경우
    );
  });

  return count + min;
}
