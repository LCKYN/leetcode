class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if(s == ""):
            return 0
        temp = [s[0]]
        for i in s[1:]:
            # print(temp)
            if(i == ")" and len(temp) > 0 and temp[-1] == "("):
                temp.pop()
            else:
                temp.append(i)
        return len(temp)