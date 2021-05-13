class Solution:
    def surfaceArea(self, g: List[List[int]]) -> int:
        
        if(len(g) == 0):
            return 0
        
        res = 0
        
        for x in range(len(g)):
            for y in range(len(g[0])):
                if(g[x][y] > 0):
                    res += g[x][y] * 4 + 2
                
                    if(x != len(g) - 1):
                        res -= min(g[x][y],g[x + 1][y]) * 2
                    if(y != len(g[0]) - 1):
                        res -= min(g[x][y],g[x][y + 1]) * 2
                            
        return res
    
    
    
    # f(0) = 0
    # f(1) = 6      
    # f(2) = 10     = f(1) + 4
    # f(3) = 14     = f(2) + 4
        