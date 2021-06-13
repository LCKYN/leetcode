class Solution:    
    def isHappy(self, n: int) -> bool:
        def f(n):
            temp = 0
            while(n):
                temp += (n % 10) ** 2 
                n //= 10
            return temp
                
        temp = set()
        while(1):
            n = f(n)
            if(n in temp):
                return False
            if(n == 1):
                return True
            temp.add(n)
