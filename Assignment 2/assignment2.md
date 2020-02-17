# CS451/CS551/EE565 Homework 2 - due Sunday February 16, 2020

You need to solve the following two problems in a programming language of your choice:

1. My free cell problem
2. Parking lot problem

For each problem, you need to define:

1. State
2. Initial State
3. Goal Test
4. Successor Function
5. 2 Heuristic Functions

For each of the problems you must write an A* algorithm that uses the problem definition and tries to solve the problem.  For each problem, I want you to define two admissible heuristics, one simple one, and another one that dominates the first one.

For each problem, you must turn in the following:

1. Your code.
2. An English description of state, initial state, goal test, successor function and 2 heuristics.
3. Program output of the solutions to the test problems that I will give you later.  For each problem there will be two outputs, one for each heuristic.  The output should show the solution to the problem, the path cost of the solution, and the number of nodes that A* examined.

Here is a description of each of the problems:

## Freecell

The problem contains blocks numbered 1 to n, one block for each number.
A state of the problem contains the following:

- A counter n.
- Several piles of blocks, each pile contains 0 to n blocks, with each block appearing exactly once.

The successor function will do one of the following things:

- Take the block on top of some pile, and place it on top of another pile, such that it is placed directly on a smaller numbered block.
- Take the block on top of some pile and place it on an empty pile.
- Take the block on top of some pile and throw it away, assuming that the number on the block matches the counter, then decrement the counter.

The problem is solved when the counter is 0, equivalently when there are no blocks left.
Any valid state could be an initial configuration.

## Parking lot Problem

You have an nxn grid. There are several cars in the grid, each car occupies two or more contiguous positions in the grid, either horizontally or vertically.  One of the cars is yours.  There is a specific position in the grid considered to be the finish.  On each step, you can move some car (either your car or one of the others) forward one space or backward one space (but not sideways), as long as no other car is there.  You have won the game when your car touches the finish position.  

I will give you my test cases after you turn in your assignment.  For now, here are some small test cases to make sure you understand what the problems are.  You can use whatever input format you like:

## Test Cases

### FreeCell

The counter is 6.  There are three piles.  Two are empty, and one is [5,4,3,2,1,6], listed from top to bottom.

### Parking lot

The grid is 4x3.  Your car is at [(2,1),(3,1)].  The other cars are at [(4,1),(4,2)] and [(2,3),(3,3),(4,3)].  You want to get your car to position (4,1).
