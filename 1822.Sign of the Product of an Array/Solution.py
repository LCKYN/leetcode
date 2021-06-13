class Solution:
    def arraySign(self, n: List[int]) -> int:
        res = False
        
        if 0 in n:
            return 0
        
        for i in n:
            if(i < 0):
                res = not res
                
        return -1 if res else 1