import numpy as np
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        
        res = [1] * 5
        m = [[0,1,0,0,0],
             [1,0,1,0,0],
             [1,1,0,1,1],
             [0,0,1,0,1],
             [1,0,0,0,0]]
        res = np.array(res)
        m = np.array(m)
        
        for _ in range(n-1):
            res = res @ m % mod
            
        return res.sum() % mod