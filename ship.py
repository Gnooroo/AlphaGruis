
class Ship():

    def __init__(self, x, y, fuel, fund):
        self.x = x
        self.y = y
        self.fuel = fuel
        self.fund = fund 
        self.crew = []
        self.cargo = []

    def move(self, dx, dy):

        if abs(dx) > abs(dy):
            distance = abs(dx)
        else:
            distance = abs(dy)

        if self.fuel >= distance:
            self.x += dx
            self.y += dy
            self.fuel -= distance

    def __str__(self):
        return f'Location:({self.x}, {self.y})\nFuel:{self.fuel}\nFund:{self.fund}\nCargo:{self.cargo}'


