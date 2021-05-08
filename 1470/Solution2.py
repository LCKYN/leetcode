class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n-1, 0, -1):
            for j in range(n-i, n):
                nums[j],nums[j+i] =nums[j+i],nums[j] 
        return nums
