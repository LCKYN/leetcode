class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        res = ""
        min_len = min(s, key = len)
        for i in range(len(min_len)):
            c = 0
            for t in s:
                # print(t, min_len[i])
                if(t[i] == min_len[i]):
                    c += 1
            if(c != len(s)):
                return res
            else:
                res += min_len[i]
                
        return res