class Solution:
    def check(self, nums: List[int]) -> bool:
        min_val = min(nums)
        size = len(nums)
        offset = nums.index(min_val)
        
        if(offset == 0):
            for i in range(size-1,-1,-1):
                if(nums[i] == min_val):
                    offset = i
                else:
                    break
        
        for i in range(1,size):
            l = (i + offset - 1) % size
            r = (i + offset) % size
            if(nums[l] > nums[r]):
                return False
        return True
            
        