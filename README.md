# CS 5820 Group Project
 Exercises 2.8 – 2.13 [1]
## What is this?
This project is designed to answer a few questions from our class textbook in regards to a "vacuum cleaner world".
In this world, we have a number of tiles.  Some are dirty and some are clean.  We implement an agent, in this case a 'vacuum cleaner', to 
go tile by tile and 'clean' all of the dirty tiles.  We try to do this in the least amount of steps possible.
## How does it work?
### The command
The program takes 3 arguements at the command line.  The arguements height, then width, then excercise number.  Once input they will be parsed 
and a decision will be made as to what excercise to run.  
### The world
No matter the excercise, we build an environment of a specific type using a list of lists, possibly measuring number of turns and collisions.  
Then we make a few of the 'tiles' in this environment dirty at random.
### The agent
Depending on the excercise, we implement any one of three types of agents: random, reflex, or state-based.  These agents act as 'vacuum 
cleaners', traversing the environment and attempting to clean all dirty tiles in the most efficient manner possible.
## How does it run?
One simply needs to have python 3.7 or 3.8 on their computer.  Then they will clone this repository onto their computer.  Finally, while in the 
directory related to this repository, they will type :
```
python3 main.py
```
Alternatively, one can simply use:
```
python main.py
```
if they do not have multiple versions of python on their computer.
