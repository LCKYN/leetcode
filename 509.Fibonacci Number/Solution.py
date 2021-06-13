class Solution:
    def fib(self, n: int) -> int:
        res = [1] * (n+1)
        res[0] = 0
        for i in range(1,n + 1):
            res[i] = res[i-1] + res[i-2]
        # print(res)
        return res[-1]