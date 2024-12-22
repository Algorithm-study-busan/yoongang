class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  push(value) {
    this.heap.push(value);
    this.heapifyUp();
  }

  heapifyUp() {
    let idx = this.size() - 1;
    while (idx > 0) {
      const parent = Math.floor((idx - 1) / 2);

      if (this.heap[idx] > this.heap[parent]) break;

      [this.heap[idx], this.heap[parent]] = [this.heap[parent], this.heap[idx]];
      idx = parent;
    }
  }

  pop() {
    if (this.size() === 1) return this.heap.pop();

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.heapifyDown();

    return value;
  }

  heapifyDown() {
    let idx = 0;
    let left = idx * 2 + 1;
    let right = idx * 2 + 2;
    let next = left;

    while (this.heap[left] || this.heap[right]) {
      if (this.heap[left] && this.heap[right]) {
        next = this.heap[left] <= this.heap[right] ? left : right;
      } else if (this.heap[right]) {
        next = right;
      }

      if (this.heap[idx] <= this.heap[next]) break;

      [this.heap[idx], this.heap[next]] = [this.heap[next], this.heap[idx]];
      idx = next;
      left = idx * 2 + 1;
      right = idx * 2 + 2;
    }
  }
}

function solution(scoville, K) {
  const h = new MinHeap();

  for (const s of scoville) {
    h.push(s);
  }

  let answer = 0;
  while (h.size() > 1 && h.heap[0] < K) {
    answer++;
    const a = h.pop();
    const b = h.pop();

    h.push(a + b * 2);
  }

  if (h.heap[0] < K) return -1;

  return answer;
}
