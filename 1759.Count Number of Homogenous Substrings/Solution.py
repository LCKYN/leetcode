class Solution:
    def countHomogenous(self, s: str) -> int:
        def f_sum(n):
            return (n*(n + 1)) // 2
        
        if(len(s) == 1):
            return 1
        
        count = 1
        res = 0
        
        for i in range(1,len(s)):
            if(s[i] == s[i-1]):
                count += 1
            else:
                res += f_sum(count)
                count = 1
                
        res += f_sum(count)
        return res % int(1e9 + 7)