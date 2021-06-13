class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0 
        res = nums[0]
        for i in nums[1:]:
            if(i != res):
                c -= 1
            else:
                c += 1
            
            if(c < 0):
                res = i
                c = 0
        return res