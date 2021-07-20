class Solution:
    def convertToTitle(self, c: int) -> str:
        if(c <= 26):
            return chr(64 + c)
        return self.convertToTitle((c - 1)//26) + chr(65 + (c-1)% 26)
        