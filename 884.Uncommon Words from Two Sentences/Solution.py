class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 += " " + s2
        s1 = s1.split(" ")
        s1 = Counter(s1)
        res = []
        for i in s1:
            if(s1[i] == 1):
                res.append(i)
        return res
        