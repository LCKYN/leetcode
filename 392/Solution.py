class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        l = len(s)
        
        if(s == ""):
            return True
        
        for i in range(len(t)):
            if(s[count] == t[i]):
                count += 1
                if(count == l):
                    return True
        return False        