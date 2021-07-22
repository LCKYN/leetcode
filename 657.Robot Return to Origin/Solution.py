class Solution:
    def judgeCircle(self, m: str) -> bool:
        v = 0
        h = 0
        for i in m:
            if(i == "U"):
                v += 1
                continue
                
                
            if(i == "D"):
                v -= 1
                continue
                
                
            if(i == "L"):
                h -= 1
                continue
                
                
            if(i == "R"):
                h += 1
                continue
                
        return h == v == 0