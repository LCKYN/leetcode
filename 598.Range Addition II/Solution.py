class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x = m
        y = n
        for i in ops:
            if(i[0] < x):
                x = i[0]
            if(i[1] < y):
                y = i[1]
        
        return x * y
        