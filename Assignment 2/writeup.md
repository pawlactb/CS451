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

    def dominating_heuristic(node):
        other_cars = node.state[1]
        goal = node.goal

        my_car = node.state[0]
        my_car_closest_spot = min(my_car, key=lambda d: distance(d, goal))

        cars_in_way = []

        if vertical(my_car):
            y = my_car_closest_spot[1]
            for car in other_cars:
                for spot in car:
                    if spot[1] == y and spot[1] in range(min(my_car_closest_spot[1], goal[0]), max(my_car_closest_spot[1], goal[1])):
                        cars_in_way.append(car)
        else:
            x = my_car_closest_spot[0]
            for car in other_cars:
                for spot in car:
                    if spot[0] == x and spot[0] in range(min(my_car_closest_spot[0], goal[0]), max(my_car_closest_spot[0], goal[0])):
                        cars_in_way.append(car)
        return len(cars_in_way) + distance(my_car_closest_spot, goal)

The dominating heuristic returns the sum of the amount of cars in the way of the goal, and the distance from the closest point of the car and the goal.

#### Dominated Heuristic

    def dominated_heuristic(node):
        return min(distance(node.state[0][0], node.goal), distance(node.state[0][1], node.goal))

The dominated heuristic returns the distance from the car to the goal.

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

    def dominating_heuristic(node):
        cost = 0
        for pile in node.state:
            if len(pile) <= 1:
                cost += len(pile)
            else:
                cost += len(pile) - 1 + len(pile)
        return cost

The dominating heuristic returns the amount of moves required to place each block in it's own pile (with an infinite amount of piles), and then discard all blocks.

#### Dominated Heuristic

    def dominated_heuristic(node):
        return sum([len(pile) for pile in node.state)

The dominated heuristic returns the amount of blocks left to be discarded.
