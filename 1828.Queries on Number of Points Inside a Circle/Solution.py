class Solution:
    def countPoints(self, p: List[List[int]], q: List[List[int]]) -> List[int]:
        res = [0] * len(q)
        for i in range(len(q)):
            for j in p:
                temp = (q[i][0]-j[0]) ** 2 + (q[i][1]-j[1]) ** 2
                temp2 = q[i][2] ** 2
                if(temp <= temp2 ):
                    res[i] += 1
        return res
        