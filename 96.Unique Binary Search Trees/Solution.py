from math import factorial
class Solution:
    def numTrees(self, n: int) -> int:
        return int(factorial(2*n)/(factorial(n)*factorial(n+1)))