class Solution:
    def coinChange(self, c: List[int], a: int) -> int:
        temp = [a + 1] * (a + 1)
        temp[0] = 0
        for i in range(len(temp)):
            for j in c:
                if(i - j >= 0):
                    temp[i] = min(temp[i], temp[i-j] + 1)
        return temp[-1] if temp[-1] != a + 1 else -1