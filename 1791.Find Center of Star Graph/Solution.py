class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        return list(set(e[0]) & set(e[1]))[0]