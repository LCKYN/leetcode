class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = "IVXLCDM"
        s = [str(t.find(i)) for i in s][::-1]
        temp = s[0]
        res = 0
        for i in s:
            n = int(i) 
            if i < temp:
                res -= (10 ** int(n/2)) * (5 if n&1 else 1)
            else :
                res += (10 ** int(n/2)) * (5 if n&1 else 1)
            temp = i
        return res