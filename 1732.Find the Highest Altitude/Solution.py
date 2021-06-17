class Solution:
    def largestAltitude(self, g: List[int]) -> int:
        g = [0] + g
        for i in range(1,len(g)):
            g[i] = g[i] + g[i-1]
        return max(g)