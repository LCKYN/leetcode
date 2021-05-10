class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l = len(nums)
        r = len(nums)
        
        for i in range(start, len(nums)):
            if(nums[i] == target):
                l = abs(i - start)
                break
        
        for i in range(start,-1,-1):
            if(nums[i] == target):
                r = abs(i - start)
                break
        return min(l,r)