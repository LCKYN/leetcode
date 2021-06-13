class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        temp = sum(a[0])
        for i in range(1, len(a)):
            temp2 = sum(a[i])
            if(temp2 > temp):
                temp = temp2
        return temp