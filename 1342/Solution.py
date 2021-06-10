class Solution:
    def numberOfSteps(self, num: int) -> int:
        if(num == 0):return 0
        res = 0
        while(num):
            if(num & 1):
                res += 1
            res +=1
            num = num >> 1
        return (res-1)
                