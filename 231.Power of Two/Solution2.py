class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n < 1): return False
        
        temp = 1
        
        while(temp < n):
            temp *= 2
        return temp == n