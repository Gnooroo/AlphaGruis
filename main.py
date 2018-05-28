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

    def do_move(self, args):
        coords = args.split(' ')
        self.ship.move(int(coords[0]), int(coords[1]))

    def do_exit(self, args):
        print("Exit")
        raise SystemExit

if __name__ == '__main__':
    console = Console()
    console.cmdloop('Starting console...')

