import argparse
import sys

from environment import *
from agent import *
from simple_reflex_agent import *
from zig_zag_vacuum import *

from directions import *

def main():
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="Implements a performance-measuring environment simulator " +
                    "for vacuum-cleaner world with modular inputs for sensors, " +
                    "actuators, and environment characteristics (size, shape, " +
                    "dirt placement) can be changed easily",
    )

    parser.add_argument(
        "--width",
        nargs=1,
        default=3,
        type=int,
        # choices=range(0,100),
        help="specify the width of the grid. defaults to 3",
    )

    parser.add_argument(
        "--height",
        nargs=1,
        default=3,
        type=int,
        # choices=range(0,100),
        help="specify the height of the grid. defaults to 3",
    )

    parser.add_argument(
        "--exercise",
        # nargs=1,
        default="2.8",
        type=str,
        choices=["2.8","2.9","2.10a","2.10b","2.10c","2.11a",
                    "2.11b","2.11c","2.11d","2.12a","2.12b"],
        help="specify the exercise to run. defaults to 2.8",
    )

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    envWidth = args.width
    envHeight = args.height
    exercise = args.exercise

    if exercise == '2.8':
        print('2.8')
    elif exercise == '2.9':
        print('2.9')
    elif exercise == '2.10a':
        print('2.10a')
    elif exercise == '2.10b':
        print('2.10b')
    elif exercise == '2.10c':
        print('2.10c')
    elif exercise == '2.11a':
        print('2.11a')
    elif exercise == '2.11b':
        print('2.11b')
    elif exercise == '2.11c':
        print('2.11c')
    elif exercise == '2.11d':
        print('2.11d')
    elif exercise == '2.12a':
        print('2.12a')
    elif exercise == '2.12b':
        print('2.12b')

    if type(envWidth) is list:
        envWidth = envWidth[0]

    if type(envHeight) is list:
        envHeight = envHeight[0]
    
    vacuumWorld = Environment(envWidth,envHeight)
    vacuumWorld.RandomizeWithoutWalls()

    vacuumWorld.Visualize()
    print("")
    reflexAgent = SimpleReflexAgent((0,0),EAST,vacuumWorld)
    reflexAgent.Run()

    print("")
    vacuumWorld.Visualize()

    print("done")

if __name__ == "__main__":
    main()
