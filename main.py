# import libraries for passing arguements at the command line
import argparse
import sys
# import all excercise methods
from environment import *
from agent import *
from simple_reflex_agent import *
from simple_reflex_with_state import *
from zig_zag_vacuum import *
from randomAgent import *
from statebot2 import *
from murphyBot import *
from faultyBot import *

# get direction constants for traversing vacuum world 
from directions import *

#sets up environment and agent for penalized movement
def twoPointTen(envWidth,envHeight):
        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("Example run of simple reflex agent")
        vacuumWorld.Visualize()
        reflexAgent = SimpleReflexAgent((0,0),EAST,vacuumWorld)
        reflexAgent.Run()
        reflexAgent.PrintLog()
        vacuumWorld.Visualize()
        
        # print header, run all variations of environment traversal
        print("\nResults of running through all possible variations:")
        results=reflexAgent.RunAllEnvironVariations()

        # print the results from running all environment traversals
        print("Percent Clean\nAvg:{}%\tMin:{}%\tMax:{}%\n".format(results["cleanAvg"],results["cleanMin"],results["cleanMax"]))
        print("Steps Taken\nAvg:{}\tMin:{}\tMax:{}\n".format(results["stepsAvg"],results["stepsMin"],results["stepsMax"]))
        print("Score\nAvg:{}\tMin:{}\tMax:{}\n\n".format(results["scoreAvg"],results["scoreMin"],results["scoreMax"]))


def main():
    # get all arguements from the command line
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="Implements a performance-measuring environment simulator " +
                    "for vacuum-cleaner world with modular inputs for sensors, " +
                    "actuators, and environment characteristics (size, shape, " +
                    "dirt placement) can be changed easily",
    )

    # getting width of the grid from the command line
    parser.add_argument(
        "--width",
        nargs=1,
        default=2,
        type=int,
        # choices=range(0,100),
        help="specify the width of the grid. defaults to 3",
    )

    # getting height of the grid from the command line
    parser.add_argument(
        "--height",
        nargs=1,
        default=1,
        type=int,
        # choices=range(0,100),
        help="specify the height of the grid. defaults to 3",
    )

    # getting excercise to run from the command line, either 8, 9, or any parts of 10, 11, or 12
    parser.add_argument(
        "--exercise",
        # nargs=1,
        default="2.8",
        type=str,
        choices=["2.8","2.9","2.10a","2.10b","2.10c","2.11a",
                    "2.11b","2.11c","2.11d","2.12a","2.12b"],
        help="specify the exercise to run. defaults to 2.8",
    )

    #error validation for insufficient number of inputs from the command line
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # assign variables for width, height, and excercise to use in the program
    args = parser.parse_args()
    envWidth = args.width
    envHeight = args.height
    exercise = args.exercise

     # only gets one width
    if type(envWidth) is list:
        envWidth = envWidth[0]
    

    # only gets one height
    if type(envHeight) is list:
        envHeight = envHeight[0]

    # checks for which excercise in the book to run
    if exercise == '2.8':
     # builds a performance measuring environment, a 'vacuum-cleaner world'
        print('2.8')
        print("Random version of vacuum world, where 1 is dirty and 0 is clean.")
        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.Visualize()
        
    elif exercise == '2.9':
    # builds a simple reflex agent to traverse an environment similar to the one
    # in excercise 2.8
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
     # prints the appropriate value
        print("Percent Clean\nAvg:{}%\tMin:{}%\tMax:{}%\n".format(results["cleanAvg"],results["cleanMin"],results["cleanMax"]))
        print("Steps Taken\nAvg:{}\tMin:{}\tMax:{}\n".format(results["stepsAvg"],results["stepsMin"],results["stepsMax"]))


    elif exercise == '2.10a':
    # runs the simple reflex agent in the penalized movement environment
        print('2.10a')
        twoPointTen(envWidth,envHeight)


    elif exercise == '2.10b':
     # runs a state-based reflex agent in the penalized movement environment
        print('2.10b')
        vacuumWorld = Environment(envWidth, envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("Example run of simple reflex with entire state agent")
        vacuumWorld.Visualize()
        reflexAgentState = StateBot2((0,0),EAST,vacuumWorld)
        reflexAgentState.Run()
        vacuumWorld.Visualize()

    elif exercise == '2.10c':
        print('2.10c')
        print("An agent that knows the status of all clean/dirty tiles cannot be rational as it is omniscient")
        print('Example')
        vacuumWorld = Environment(envWidth, envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.Visualize()
        reflexAgentEntireState = SimpleReflexAgentWithEntireState((0,0),EAST,vacuumWorld)
        reflexAgentEntireState.Run()
        reflexAgentEntireState.PrintDirtyTiles()
        vacuumWorld.Visualize()

    elif exercise == '2.11a':
        print('2.11a')
        print('A simple reflex agent can still be rational in an unknown environment, as it is still acting logically on its percepts')
        print('Example')
        vacuumWorld = Environment(envWidth, envHeight)
        vacuumWorld.RandomizeWithWalls()
        vacuumWorld.Visualize()
        agent = SimpleReflexAgent((0,0),EAST,vacuumWorld)
        agent.Run()
        vacuumWorld.Visualize()

    elif exercise == '2.11b':
        print('2.11b')
        #Can a simple reﬂex agent with a randomized agent function outperform a simple reﬂex agent?
        #Design such an agent and measure its performance on several environments.
        print('NOTE: 2 in the grid represents a wall')
        vacuumWorld = Environment(5,5)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.SetWallsFromBinary(9439748)
        vacuumWorld.Visualize()

        randomAgent = RandomAgent((0,0),EAST,vacuumWorld)
        randomAgent.Run()

        #randomAgent.PrintLog()

        vacuumWorld.Visualize()

        vacuumWorld = Environment(5,5)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.SetWallsFromBinary(9439748)
        vacuumWorld.Visualize()

        randomAgent = RandomAgent((0,0),EAST,vacuumWorld)
        randomAgent.Run()

        #randomAgent.PrintLog()

        vacuumWorld.Visualize()
        print("*******************************************")

        vacuumWorld = Environment(5,5)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.SetWallsFromBinary(145536)
        vacuumWorld.Visualize()

        randomAgent = RandomAgent((0,0),EAST,vacuumWorld)
        randomAgent.Run()

        #randomAgent.PrintLog()

        vacuumWorld.Visualize()

        print("*******************************************")

        vacuumWorld = Environment(5,5)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.SetWallsFromBinary(15360)
        vacuumWorld.Visualize()

        randomAgent = RandomAgent((0,0),EAST,vacuumWorld)
        randomAgent.Run()

        #randomAgent.PrintLog()

        vacuumWorld.Visualize()

    elif exercise == '2.11c':
        print('2.11c')
        # environment designed to make our agent not behave rationally
        vacuumWorld = Environment(5,5)
        vacuumWorld.RandomizeWithoutWalls()
        vacuumWorld.SetWallsFromBinary(16864)
        vacuumWorld.Visualize()

        randomAgent = RandomAgent((0,0),EAST,vacuumWorld)
        randomAgent.Run()

        #randomAgent.PrintLog()

        vacuumWorld.Visualize()

        print("Note how unlikely the agent is to pass around the wall with a 1 tile gap")
    elif exercise == '2.11d':
        print('2.11d')


        # trial 1
        #************************************************************************************************
        simpleWorld = Environment(5,5)
        stateWorld = Environment(5,5)
        
        simpleWorld.SetGridFromBinary(23821635)
        simpleWorld.SetWallsFromBinary(480)
        
        stateWorld.SetGridFromBinary(23821635)
        stateWorld.SetWallsFromBinary(480)

        print("TRIAL 1\nBEFORE")
        simpleWorld.Visualize()

        simpleAgent = SimpleReflexAgent((0,0),EAST,simpleWorld)
        stateAgent = StateBot2((0,0),EAST,stateWorld)

        simpleAgent.Run()
        stateAgent.Run()

        print("AFTER")
        print("With state")
        stateWorld.Visualize()
       
        print("Without state")
        simpleWorld.Visualize()
        
        resultsWithoutState = simpleWorld.GetPerformanceMeasure()
        resultsWithState = stateWorld.GetPerformanceMeasure()

        # trial 2
        #************************************************************************************************

        # TODO: Run reflex agent vs state-based agent on multiple environments and run comparison on efficiency FINISH

    elif exercise == '2.12a':
        print('2.12a')
        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("Murphy's Law")
        vacuumWorld.Visualize()
        agent = MurphyBot((0,0),EAST,vacuumWorld)
        agent.Run()
        vacuumWorld.Visualize()

        vacuumWorld = Environment(envWidth,envHeight)
        vacuumWorld.RandomizeWithoutWalls()
        print("With a faulty dirt sensor")
        vacuumWorld.Visualize()
        agent = FaultyBot((0,0),EAST,vacuumWorld)
        agent.Run()
        vacuumWorld.Visualize()

    elif exercise == '2.12b':
        # TODO: create agent that will run in environment will clean square has a 10% chance of getting dirty
        print('2.12b')

    print("done")

if __name__ == "__main__":
    main()
