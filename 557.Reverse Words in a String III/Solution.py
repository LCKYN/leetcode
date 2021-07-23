class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        return " ".join([i[::-1] for index,i in enumerate(s)])
        