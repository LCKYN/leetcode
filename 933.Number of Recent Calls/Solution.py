class RecentCounter:

    def __init__(self):
        self.temp = list()
        self.i = 0
        self.l = 0
        

    def ping(self, t: int) -> int:
        self.temp.append(t)
        self.l += 1
        while(self.temp[self.i] < t - 3000):
            self.i += 1
        return self.l - self.i
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)