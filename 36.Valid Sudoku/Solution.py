import numpy as np
class Solution:
    def isValidSudoku(self, b: List[List[str]]) -> bool:
        b = np.array(b).reshape(81)
        
        for i in range(9):
            start = i * 9
            stop = i * 9 + 9            
            temp = b[start:stop]

            _,c = np.unique(temp[temp != "."],return_counts=True)
            
            if(c.sum() != c.shape[0]):
                return False
            
        for i in range(9):
            temp = b[i:81:9]
            
            _,c = np.unique(temp[temp != "."],return_counts=True)
            
            if(c.sum() != c.shape[0]):
                return False
        
        for i in [1,4,7,28,31,34,55,58,61]:
            a = np.array([1,2,3,10,11,12,19,20,21])
            
            temp = b[(a + i - 2)]
            
            _,c = np.unique(temp[temp != "."],return_counts=True)
            
            if(c.sum() != c.shape[0]):
                return False
        return True