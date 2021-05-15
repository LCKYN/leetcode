class Solution:
    def numberOfMatches(self, n: int) -> int:
        if(n == 1):
            return 0
        temp = 0 if(n % 2 == 0 ) else 1
        return n // 2 + self.numberOfMatches(n//2 + temp)
        