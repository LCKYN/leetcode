class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0): 
            return False
        if(x < 10): 
            return True
        x1 = x
        x2 = 0
        
        while(x1):
            
            x2 *= 10
            x2 += x1 % 10
            x1 //= 10
        
            if(x == x2):
                return True
        return False
        
        