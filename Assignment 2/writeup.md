# Assignment 2

## Parkinglot

### state

State in this problem is a tuple.

    (my_car, other_cars)

where each car is a list of coordinates i.e.

    my_car = [(1,2), (2,2)]
    other_cars = [[(3,2), (2,2)], [(4,5), (5,5)]]

my_car is a singular car, other_cars is a list of cars.

### initial state

The initial state is the initial configuration of the board as per the test cases. Any valid state is a valid initial state.

### goal test

The goal checks to see if the goal coordinate is in the my_car part of state. It also checks that the state is valid to ensure we are not accidentally accepting an invalid state.

### successor function

The successor function lists every possible move for my_car, and for each car in other_cars, including invaid moves. The is_valid() function is used to exclude invalid states from being considered in the A* search.

### Heuristics

#### Dominating Heuristic

The dominating heuristic returns the distance from the goal to the closest part of my_car.

#### Dominated Heuristic

The dominated heuristic returns infinity if there is a car in the way, and 1 otherwise. This heuristic is inadmissable in some circumstances.

----

## FreeCell

### state

Here, state is represented as a list of lists to represent the piles, and an int to represent the counter. Each internal list is a pile of blocks, used as a stack.

### initial state

Any valid state is a valid initial state.

### goal test

The goal_test() function checks to see if all of the piles are empty and that the counter is equal to zero.

### successor function

The successor function will return a list of states possible from moving/discarding the top of each pile to each other valid placement on another pile, or a valid discard.

### Heuristics

#### Dominating Heuristic

The dominating heuristic returns the amount of moves required to perform the next discard.

#### Dominated Heuristic

The dominated heuristic returns the amount of blocks left to be discarded.
