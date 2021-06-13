class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        count = 1
        for i in range(1,len(s)):
            if(s[i-1] == s[i]):
                count += 1
            else:
                if(count > res):
                    res = count
                count = 1
        if(count > res):
            res = count
        return res
        