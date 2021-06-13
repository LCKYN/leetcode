class Solution:
    def isValid(self, s: str) -> bool:
        t = []
        for i in s:
            if i in "{[(":
                t.append(i)
            else:
                if(len(t) == 0): return False
                temp = t.pop()
                if(temp == "(" and i != ")"):
                    return False
                if(temp == "{" and i != "}"):
                    return False
                if(temp == "[" and i != "]"):
                    return False
                
        return len(t) == 0