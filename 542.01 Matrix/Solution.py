class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if(mat[y][x] != 0):
                    mat[y][x] = len(mat) + len(mat[y])
                
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                if(mat[y][x] == 0): continue
                temp = len(mat) + len(mat[y])
                
                if(x > 0):
                    temp = min(temp,mat[y][x-1] + 1)
                if(x < len(mat[y]) - 1):
                    temp = min(temp,mat[y][x+1] + 1)
                
                if(y > 0):
                    temp = min(temp,mat[y-1][x] + 1)
                if(y < len(mat) - 1):
                    temp = min(temp,mat[y+1][x] + 1)
                    
                mat[y][x] = temp
        
        for y in range(len(mat))[::-1]:
            for x in range(len(mat[y]))[::-1]:
                if(mat[y][x] == 0): continue
                temp = len(mat) + len(mat[y])
                
                if(x > 0):
                    temp = min(temp,mat[y][x-1] + 1)
                if(x < len(mat[y]) - 1):
                    temp = min(temp,mat[y][x+1] + 1)
                
                if(y > 0):
                    temp = min(temp,mat[y-1][x] + 1)
                if(y < len(mat) - 1):
                    temp = min(temp,mat[y+1][x] + 1)
                    
                mat[y][x] = temp
                


        return mat