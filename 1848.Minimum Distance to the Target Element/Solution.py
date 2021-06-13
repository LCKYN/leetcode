class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = []
        for i in range(len(nums)):
            if(nums[i] == target):
                res.append(abs(i - start))
        return min(res)