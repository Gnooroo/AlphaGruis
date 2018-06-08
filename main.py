from cmd import Cmd
from map import Map
from ship import Ship

class Console(Cmd):

    prompt = '> '

    def __init__(self):
        super(Console, self).__init__()

        self.map = Map(10, 10)
        self.ship = Ship(5, 5, 10, 100)

    def do_hello(self, args):
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args

        print("hello, %s" % name)

    def do_map(self, args):
        self.map.draw()

    def do_ship(self, args):
        print(self.ship)


    def do_m(self, args):
        self.do_move(args)

    def do_move(self, args):
        d = args[0].lower()
        if d == 'e' or d == 'east':
            dx, dy = 1, 0
        elif d == 'ne' or d == 'northeast':
            dx, dy = 1, 1
        elif d == 'n' or d == 'north':
            dx, dy = 0, 1
        elif d == 'nw' or d == 'northwest':
            dx, dy = -1, 1
        elif d == 'w' or d == 'west':
            dx, dy = -1, 0
        elif d == 'sw' or d == 'southwest':
            dx, dy = -1, -1
        elif d == 's' or d == 'south':
            dx, dy = 0, -1
        elif d == 'se' or d == 'southeast':
            dx, dy = 1, -1

        self.ship.move(dx, dy)
        print(f'New Location: ({self.ship.x}, {self.ship.y})')

    def do_exit(self, args):
        print("Exit")
        raise SystemExit

if __name__ == '__main__':
    console = Console()
    console.cmdloop('Starting console...')

