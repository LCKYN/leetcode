class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        count = 1
        digits = [0] + digits
        digits[-count] += 1
        
        while(digits[-count] == 10 and count < len(digits)):
            digits[-count] = 0
            count += 1
            digits[-count] += 1
            
        if(digits[0] == 0):
            digits = digits[1:]
            
        return digits