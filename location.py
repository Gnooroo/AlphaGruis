import random

class Location():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.value = random.randrange(100)
        self.scanned = False
        self.visited = False

    def __str__(self):
        return str(f'{self.value:02}')
