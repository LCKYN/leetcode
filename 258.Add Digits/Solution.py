class Solution:
    def addDigits(self, n: int) -> int:
        if(n < 10):
            return n
        temp = n % 9
        if(temp):
            return temp
        return 9