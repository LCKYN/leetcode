class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[0:n]
        y=nums[n:2*n]
        res=[0]*(n*2)

        for i in range(n):
            t = i<<1
            res[t] = x[i]
            res[t + 1] = y[i]

        return(res)