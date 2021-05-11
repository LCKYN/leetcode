class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        temp = (max(A) - K) - (min(A) + K)
        temp = max(temp,0)
        return temp
        