class Solution:
    def maxProduct(self, n: List[int]) -> int:
        m1 = 0
        for i in range(1, len(n)):
            if(n[i] > n[m1]):
                m1 = i
        m2 = m1-1
        for i in range(len(n)):
            if(n[i] > n[m2] and m1 != i):
                m2 = i
        # print(m1,m2)
        return (n[m1]-1) * (n[m2]-1)