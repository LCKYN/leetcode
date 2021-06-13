class Solution:
    def checkIfPangram(self, s: str) -> bool:
        return 26 == len(set(s))
        