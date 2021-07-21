class Solution:
    def myAtoi(self, s: str) -> int:
        state = 0
        si = 1
        res = 0
        i = 0
        while(i < len(s)):
            
            res *= 10
            
            if(state == 0):
                if(s[i] == " "):
                    i += 1
                else:
                    state = 1
            elif(state == 1):
                if(s[i] == "-"):
                    si = -1
                    i += 1
                elif(s[i] == "+"):
                    i += 1
                state = 2
            elif(state == 2):
                if('0' <= s[i] <= "9"):
                    res += ord(s[i]) - 48
                    i += 1
                else:
                    res //= 10
                    break
               
        res = res * si
        if(res < 0):
            res = max(res, -2 ** 31)
        else:
            res = min(res, 2 ** 31 - 1)
        
        return res