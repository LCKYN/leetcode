class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_nums = sorted(nums)
        found = False
        l = 0
        r = len(nums) - 1
        
        while(not found):
            if(s_nums[r] + s_nums[l] > target):
                r -= 1
            elif(s_nums[r] + s_nums[l] < target):
                l += 1
            else:
                found = True
                
        res = [-1,-1]
        for i in range(len(nums)):
            if(nums[i] == s_nums[l] and res[0] == -1):
                res[0] = i
            elif(nums[i] == s_nums[r]):
                res[1] = i
        
        return res
                