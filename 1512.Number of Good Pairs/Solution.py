class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums).items()
        res = 0
        for i in c:
            n = i[1]
            res += n * (n-1) // 2
        return(res) 