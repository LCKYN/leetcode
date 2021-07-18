class Solution:
    def titleToNumber(self, c: str) -> int:
        if(len(c) == 1):
            return ord(c) - 64
        return self.titleToNumber(c[:-1]) * 26 + ord(c[-1]) - 64
            