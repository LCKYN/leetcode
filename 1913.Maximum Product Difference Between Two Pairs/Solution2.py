class Solution:
    def maxProductDifference(self, n: List[int]) -> int:
        max_ = [0,0]
        min_ = [2e4,2e4]
        
        for i in n:
            if(i > max_[0]): 
                max_[0], max_[1] = i, max_[0]
            elif(i > max_[1]):
                max_[1] = i
                
            if(i < min_[0]): 
                min_[0], min_[1] = i, min_[0]
            elif(i < min_[1]):
                min_[1] = i
                
        return max_[0] * max_[1] - min_[0] * min_[1]
                