from collections import deque

class Solution:
    def isNext(self, str1, str2):
        count = 0
        for i in range(8):
            if str1[i] == str2[i]:
                count += 1
        
        return True if count == 7 else False

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if len(bank) == 0:
            if startGene == endGene: return 0
            return -1

        visited = [False for _ in range(len(bank))]

        q = deque()
        q.append((startGene, 0))

        while q:
            ngene, nresult = q.popleft()
            if ngene == endGene:
                return nresult
                
            for i in range(len(bank)):
                if not visited[i] and self.isNext(ngene, bank[i]):
                    q.append((bank[i], nresult + 1))
                    visited[i] = True

        return -1