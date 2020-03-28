from node import Node

from search import a_star
from copy import deepcopy

from collections import Counter


def intersection(car1, car2):
    return len([spot for spot in car1 if spot in car2]) != 0


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def vertical(car):
    # vertical cars all have the same x coordinate
    return all(x_coord == car[0][0] for x_coord, _ in car)


def moves(car):
    ret_val = []
    if vertical(car):
        # car can either move up or down one space
        for t in [1, -1]:
            ret_val.append([(x, y+t) for x, y in car])
    else:
        # car can either move left or right one space
        for t in [1, -1]:
            ret_val.append([(x+t, y) for x, y in car])

    return ret_val


class ParkinglotNode(Node):
    def __init__(self, dimensions, goal, state=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.dimensions = dimensions
        self.goal = goal
        # here, we view state as a 2-tuple with the first element being "our car"
        # and the 2nd element being the other cars on the grid
        if state == None:
            self.state = ((0, 0), [])
        else:
            self.state = deepcopy(state)

    def __str__(self):
        return "My Car: %s Other Cars: %s Goal: %s Path: %s" % (str(self.state[0]), str(self.state[1]), str(self.goal), self.path)

    def __lt__(self, other):
        return distance(self.state[0][0], self.goal) > distance(other.state[0][0], other.goal)

    def __eq__(self, other):
        if self.state[0] != other.state[0]:
            return False

        for car in self.state[1]:
            if car not in other.state[1]:
                return False

        return True

    def goal_test(self):
        return self.goal in self.state[0]

    def is_valid(self):
        my_car = self.state[0]
        other_cars = self.state[1]

        cars = [] + [my_car] + other_cars
        for car in cars:
            for other_car in cars:
                if car == other_car:
                    continue

                if intersection(car, other_car):
                    return False

                for x, y in car:
                    if x > self.dimensions or x <= 0 or y > self.dimensions or y <= 0:
                        return False
        return True

    def successors(self):
        ret_val = []

        my_car = self.state[0]
        other_cars = self.state[1]

        # first, add the moves of our car to the successors
        for car in moves(my_car):
            n = ParkinglotNode(dimensions=self.dimensions,
                               goal=self.goal,
                               state=(car, other_cars),
                               path=self.path + ["%s -> %s" % (my_car, car)])
            if n.is_valid():
                ret_val.append(n)
            # else:
            #     print("Invalid state: %s" % (str(n.state)))

        # next, add possible moves for the other cars
        for car in other_cars:
            # keep a list of cars without the current, so we can append the moves of cars
            cars_wo_current = other_cars[:]
            cars_wo_current.remove(car)
            # print(cars_wo_current)
            n = None
            for move in moves(car):
                n = ParkinglotNode(dimensions=self.dimensions,
                                   goal=self.goal,
                                   state=(my_car, cars_wo_current + [move]),
                                   path=self.path + ["%s -> %s" % (car, move)])

                if n.is_valid():
                    ret_val.append(n)

        return ret_val


# def dominating_heuristic(node):
#     my_car = node.state[0]
#     other_cars = node.state[1]

#     intersections = 0

#     if vertical(my_car):
#         # we're travelling in y
#         for y in range(min(my_car[0][1], node.goal[1]), max(my_car[0][1], node.goal[1]) + 1):
#             point = (my_car[0][0], y)
#             for car in other_cars:
#                 if intersection(point, car):
#                     intersections += 1
#     else:
#         # we're traveling in x
#         for x in range(min(my_car[0][0], node.goal[0]), max(my_car[0][0], node.goal[0]) + 1):
#             point = (x, my_car[0][1])
#             for car in other_cars:
#                 if intersection(point, car):
#                     intersections += 1
#     return intersections


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


def dominated_heuristic(node):
    return min(distance(node.state[0][0], node.goal), distance(node.state[0][1], node.goal))


def cost_fn(n): return len(n.path)


def main():
    test_no = 0
    # test case format: (my_car, other_cars, dimensions)
    test_cases = [([(1, 2), (2, 2)], [[(4, 5), (5, 5)], [(4, 1), (4, 2), (4, 3)], [(2, 4), (2, 5)]], 5, (5, 2)),
                  ([(3, 3), (3, 4)], [[(1, 2), (1, 3)], [(1, 5), (1, 6)], [(2, 2), (3, 2)], [(1, 4), (2, 4)], [(2, 6), (3, 6)], [(4, 6), (5, 6)]], 6, (3, 6))]

    for my_car, other_cars, dimensions, goal in test_cases:
        test_no += 1
        initial_state = (my_car, other_cars)
        print("\nTest Case: %d, %s" % (test_no, initial_state))

        root = ParkinglotNode(dimensions=dimensions, goal=goal,
                              state=initial_state, path=[])

        print("Root Initial State: %s" % (str(root.state)))

        print("Running A* using the Dominating Heuristic:")
        print("Node: %s\n Total Nodes Examined: %d" %
              (a_star(root, dominating_heuristic, cost_fn, node_count_max=5000)))

        print("Running A* using the Dominated Heuristic:")
        print("Node: %s\n Total Nodes Examined: %d" %
              (a_star(root, dominated_heuristic, cost_fn, node_count_max=5000)))

        del root


if __name__ == "__main__":
    main()
