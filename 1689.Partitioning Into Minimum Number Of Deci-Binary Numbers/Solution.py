class Solution:
    def minPartitions(self, n: str) -> int:
        temp = Counter(n).items()
        temp = [int(i[0]) for i in temp]
        return max(temp)