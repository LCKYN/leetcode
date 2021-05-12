class Solution:
    def smallerNumbersThanCurrent(self, a: List[int]) -> List[int]:
        max_ = max(a)
        min_ = min(a)
        temp = [0] * (max_ - min_ + 2)
        
        for i in a:
            temp[i - min_ + 1] += 1 
            
        for i in range(1, len(temp)):
            temp[i] += temp[i - 1]
            
        for i in range(len(a)):
            a[i] = temp[a[i]- min_]
        
        return a
            