class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c1 = not (n & (n-1))
        c2 = n > 0
        return c1 and c2