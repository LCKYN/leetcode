class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0): return 0
        l = 0
        r = 0
        temp = set()
        max_len = 1
        while(r < len(s)):
            # print(r, s[r], temp, (not s[r] in temp))
            if(not s[r] in temp):
                temp.add(s[r])
                if(len(temp) > max_len):
                    max_len = len(temp)
                r += 1
            else:
                # print(temp)
                if(s[r] != s[l]):
                    temp.remove(s[l])
                else:
                    r += 1
                l += 1    
        return max_len