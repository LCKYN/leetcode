class Solution:
    def createTargetArray(self, n: List[int], i: List[int]) -> List[int]:
        res = []
        for _ in range(len(i)) :
            res.insert(i[_],n[_])
        return res
        