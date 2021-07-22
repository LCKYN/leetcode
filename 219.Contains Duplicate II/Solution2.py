class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = dict()
    
        for i, n in enumerate(nums):
            if n in temp and i - temp[n] <= k:
                return True
            
            temp[n] = i
            
        return False
