class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        len_y, len_x = len(mat), len(mat[0])
        res =[[0 for _ in range(len_y)] for _ in range(len_x)]
        
        for y in range(len_y):
            for x in range(len_x):
                res[x][y] = mat[y][x]
        return res