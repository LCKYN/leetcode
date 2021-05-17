class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        l = 0
        r = len(n)-1
        while(1):
            if(n[l] + n[r] < t):
                l += 1
            elif(n[l] + n[r] > t):
                r -= 1
            else:
                return [l+1,r+1]