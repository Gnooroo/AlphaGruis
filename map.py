from location import Location

class Map():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Location(x, y) for x in range(width)] for y in range(height)]

    def draw(self):
        output = ''

        for y in range(self.height):
            for x in range(self.width):
                output += str(self.grid[x][y]) + ' '

            output += '\n'

        print(output)
