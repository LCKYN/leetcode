class Solution:
    def kidsWithCandies(self, c: List[int], e: int) -> List[bool]:
        temp = max(c)
        res = [False] * len(c)
        for i in range(len(c)):
            res[i] = c[i] + e >= temp
        return res
        