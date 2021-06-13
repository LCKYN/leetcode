class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if(s == ""):
            return 0
        temp = [s[0]]
        for i in s[1:]:
            if(i == ")" and len(temp) > 0 and temp[-1] == "("):
                del temp[-1]
            else:
                temp.append(i)
        return len(temp)