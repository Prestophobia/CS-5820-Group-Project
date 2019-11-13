import argparse
import sys

from environment import *
from agent import *
from simple_reflex_agent import *
from simple_reflex_with_state import *
from zig_zag_vacuum import *

from directions import *

def twoPointTen(envWidth,envHeight):
        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("Example run of simple reflex agent")
        vacuumWorld.Visualize()
        reflexAgent = SimpleReflexAgent((0,0),EAST,vacuumWorld)
        reflexAgent.Run()
        reflexAgent.PrintLog()
        vacuumWorld.Visualize()

        print("\nResults of running through all possible variations:")
        results=reflexAgent.RunAllEnvironVariations()

        print("Percent Clean\nAvg:{}%\tMin:{}%\tMax:{}%\n".format(results["cleanAvg"],results["cleanMin"],results["cleanMax"]))
        print("Steps Taken\nAvg:{}\tMin:{}\tMax:{}\n".format(results["stepsAvg"],results["stepsMin"],results["stepsMax"]))
        print("Score\nAvg:{}\tMin:{}\tMax:{}\n\n".format(results["scoreAvg"],results["scoreMin"],results["scoreMax"]))


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
        default=2,
        type=int,
        # choices=range(0,100),
        help="specify the width of the grid. defaults to 3",
    )

    parser.add_argument(
        "--height",
        nargs=1,
        default=1,
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

    if type(envWidth) is list:
        envWidth = envWidth[0]

    if type(envHeight) is list:
        envHeight = envHeight[0]

    if exercise == '2.8':
        print('2.8')
        print("Random version of vacuum world, where 1 is dirty and 0 is clean.")
        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.Visualize()
    elif exercise == '2.9':
        print('2.9')
        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("Example run of simple reflex agent")
        vacuumWorld.Visualize()
        reflexAgent = SimpleReflexAgent((0,0),EAST,vacuumWorld)
        reflexAgent.Run()
        reflexAgent.PrintLog()
        vacuumWorld.Visualize()
        print()
        print("Results of running through all possible variations:")
        results=reflexAgent.RunAllEnvironVariations()

        print("Percent Clean\nAvg:{}%\tMin:{}%\tMax:{}%\n".format(results["cleanAvg"],results["cleanMin"],results["cleanMax"]))
        print("Steps Taken\nAvg:{}\tMin:{}\tMax:{}\n".format(results["stepsAvg"],results["stepsMin"],results["stepsMax"]))


    elif exercise == '2.10a':
        print('2.10a')
        twoPointTen(envWidth,envHeight)

    elif exercise == '2.10b':
        print('2.10b')

        vacuumWorld = Environment(envWidth, envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("Example run of simple reflex with entire state agent")
        vacuumWorld.Visualize()
        reflexAgentEntireState = SimpleReflexAgentWithEntireState((0,0),EAST,vacuumWorld)
        reflexAgentEntireState.Run()
        reflexAgentEntireState.PrintDirtyTiles()

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


    vacuumWorld = Environment(envWidth,envHeight)
    vacuumWorld.RandomizeWithoutWalls()
    print("done")

if __name__ == "__main__":
    main()
