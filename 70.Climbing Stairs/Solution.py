class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 1, 2]
        n -= 2
        for i in range(n):
            res[i%3] = res[(i+1)%3] + res[(i+2)%3]
        return res[(n+2)%3]