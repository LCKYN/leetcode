import numpy as np

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.r = np.array(rectangle)

    def updateSubrectangle(self, r1: int, c1: int, r2: int, c2: int, val: int) -> None:
        self.r[r1:r2+1,c1:c2+1] = val

    def getValue(self, r: int, c: int) -> int:
        return self.r[r,c]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)