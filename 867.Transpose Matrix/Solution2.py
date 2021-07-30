class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        len_y, len_x = len(mat), len(mat[0])
        res =[[mat[y][x] for y in range(len_y) ]for x in range(len_x)]
        return res