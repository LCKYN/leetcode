class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def f(t,n):
            b = dict()
            b["2"] = "abc"
            b["3"] = "def"
            b["4"] = "ghi"
            b["5"] = "jkl"
            b["6"] = "mno"
            b["7"] = "pqrs"
            b["8"] = "tuv"
            b["9"] = "wxyz"
            if(n == ""):
                return [t]
            # for i in b[n[0]]:
                
            if(n[0] in "79"):
                return f(t+b[n[0]][0], n[1:]) + f(t+b[n[0]][1], n[1:]) + f(t+b[n[0]][2], n[1:]) + f(t+b[n[0]][3], n[1:]) 
            
            return f(t+b[n[0]][0], n[1:]) + f(t+b[n[0]][1], n[1:]) + f(t+b[n[0]][2], n[1:])

        if(digits == ""):return []
        return (f("",digits))