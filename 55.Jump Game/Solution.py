
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums) == 1): return True
        
        nums = nums[:-1]
        
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] - 1, nums[i])
        
        for i in nums:
            if(i == 0):
                return False
            
        return True
            