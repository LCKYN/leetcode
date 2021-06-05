class ParkingSystem:

    def __init__(self, l: int, m: int, s: int):
        self.p = [0, l, m, s]

    def addCar(self, t: int) -> bool:
        if(self.p[t]):
            self.p[t] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)