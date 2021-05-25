class Solution:
    def countPrimes(self, n: int) -> int:
        if(n < 2):
            return 0
        
        temp = [True] * (n)
        temp[0] = False
        temp[1] = False
        
        for i in range(2,int(n**0.5) + 1):
            
            if(temp[i]):
                
                m = i * i

                while(m < n):
                    temp[m] = False
                    m += i
                
        return sum(temp)
        