class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        o = list()
        e = list()
        
        for i in nums:
            if(i & 1):
                o.append(i)
            else:
                e.append(i)
    
        return e + o[::-1]
                