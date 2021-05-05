class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        m = 1
        if x < 0:
            x = -x
            m = -1
        while x>0:
            res *= 10
            res += x % 10
            x //= 10
        if(res>>31):
            return 0
        return(m * res)
        