class Solution:
    def canBeEqual(self, t: List[int], a: List[int]) -> bool:
        return sum(a) == sum(t) and set(a) == set(t)
        