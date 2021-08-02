class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        
        e = 0
        o = l - 1
        
        for i in nums:
            if(i & 1):
                res[o] = i
                o -= 1
            else:
                res[e] = i
                e += 1
                
        return res
            
                