class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        r = Counter(r)
        m = Counter(m)
        
        for i in r:
            if(r[i] >m[i]):
                return False
        return True
        