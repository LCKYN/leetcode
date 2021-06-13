class Solution:               
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def fill(res):
            if(len(res) > 1):
                if(res[-1] == res[-2]):
                    return res[-1]
            return ""

        def fill2(n):
            sl = sorted(l)

            if(l[0] == sl[-1] and n != 'a' and l[0] > 0):
                l[0] -= 1
                return 'a'
            if(l[1] == sl[-1] and n != 'b' and l[1] > 0):
                l[1] -= 1
                return 'b'
            if(l[2] == sl[-1] and n != 'c' and l[2] > 0):
                l[2] -= 1
                return 'c'

            if(l[0] == sl[-2]  and l[0] > 0):
                l[0] -= 1
                return 'a'
            if(l[1] == sl[-2]  and l[1] > 0):
                l[1] -= 1
                return 'b'
            if(l[2] == sl[-2]  and l[2] > 0):
                l[2] -= 1
                return 'c'
            return ""    
        res = ""
        l = [a, b, c]
        
        while(sum(l) > 0):
            n = fill(res)
            
            temp = fill2(n)
            
            if(temp == ""):break
            
            res += temp
            print(res)
        return res
            
                
