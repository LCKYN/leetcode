class Solution:
    def partitionDisjoint(self, nums: List[int], i = 0) -> int:
        res = nums.index(min(nums)) + 1
        max_l = max(nums[:res])
        min_r = min(nums[res:])
        while(max_l > min_r):
            temp = nums[res:]
            print(temp)
            res = res + temp.index(min_r) + 1
            max_l = max(nums[:res])
            min_r = min(nums[res:])
        return res