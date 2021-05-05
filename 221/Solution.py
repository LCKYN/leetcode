class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        for y in range(1, len(m)):
            for x in range(1, len(m[0])):
                m[y][x] = (min(int(m[y][x-1]), int(m[y-1][x]), int(m[y-1][x-1])) + 1) * int(m[y][x])
                
        max_size = 0
        for y in range(len(m)):
            for x in range(len(m[0])):
                if(int(m[y][x]) > max_size):
                    max_size = int(m[y][x])

        return max_size * max_size