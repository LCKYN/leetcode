import math as m
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if(int(m.log10(i)) & 1):
                res += 1
        return res
        