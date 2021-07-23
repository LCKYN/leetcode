class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return "".join([s[i:i+k][::-1] if (i + k)//k & 1 else s[i:i+k] for i in range(0,len(s),k)])
        