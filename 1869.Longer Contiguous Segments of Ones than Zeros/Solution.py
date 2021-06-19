class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        s += 'a'
        l = 0
        r = 0
        a = 0
        b = 0
        while(r < len(s)):
            if(s[l] != s[r]):
                if(s[l] == '0'):
                    a = max(a, r-l)
                else:
                    b = max(b, r-l)
                l = r
            r += 1
        return b > a