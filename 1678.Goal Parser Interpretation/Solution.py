class Solution:
    def interpret(self, c: str) -> str:
        res = ""
        i = 0
        while(i < len(c)):
            if(c[i] == "("):
                if(c[i + 1] == ")"):
                    res +=  "o"
                    i += 1
                else:
                    res += "al"
                    i += 3
            else:
                res += c[i]
            i += 1
        return res