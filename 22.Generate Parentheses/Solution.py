class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(l,r,c,t):
            if(l == 0 and r == 0):
                res.append(t)
            else:
                if(l != 0):
                    f(l-1,r,c + 1,t+"(")
                if(r != 0 and c > 0):
                    f(l,r-1,c-1,t+")")
                
        res = list()
        f(n,n,0,"")

        return res
