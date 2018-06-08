

class Building():

    def __init__(self, name):
        self.name = name 
        

    def __str__(self):
        return f'Name: {self.name}'
    

class Factory(Building):

    def __init__(self):
        Building.__init__(self, type(self).__name__)


