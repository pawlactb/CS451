from node import Node
from search import a_star
from copy import deepcopy


def pile_helper(src, dest, state):
    """Return the state after moving from one pile to another.

    Arguments:
        src {int} -- the index of the pile to move from
        dest {int} -- the index of the pile to move to
        state {list} -- the current state (const)
    """
    new_state = deepcopy(state)

    if dest is not None:
        new_state[dest].append(new_state[src].pop())
    else:
        new_state[src].pop()
    return new_state


class FreeCellNode(Node):
    def __init__(self, counter, n, state=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = counter

        if state is None:
            self.state = []
            for _ in range(0, n):
                self.state += [[]]
        else:
            for pile in state:
                pile.reverse()

            self.state = deepcopy(state)

    def __lt__(self, other):
        return len(self.path) < len(other.path)

    def __str__(self):
        return ("Counter: %d State: %s Path: %s" % (self.counter, str(self.state), str(self.path)))

    def is_valid(self):
        return True

    def is_complete(self):
        complete = True
        for stack in self.state:
            if len(stack) is not 0:
                complete = False
        return complete

    def goal_test(self):
        return self.counter == 0 and self.is_complete()

    def successors(self):
        successors = []
        for pile_num, pile in enumerate(self.state):
            # if the pile is empty, skip it
            if len(pile) == 0:
                continue

            # if the pile isn't empty, check to see if we can put it on top of another pile
            for other_pile_num, other_pile in enumerate(self.state):
                # if we're looking at the same piles, this won't make a new state. Continue.
                if other_pile_num == pile_num:
                    continue

                # discard
                if pile[-1] == self.counter:
                    successors.append(FreeCellNode(
                        counter=self.counter - 1,
                        n=len(self.state),
                        state=pile_helper(
                            pile_num, None, self.state),
                        parent=self,
                        path=(self.path + ["Discard: %d" % (pile[-1])])))

                # we can place anything on top of an empty pile
                if len(other_pile) == 0:
                    successors.append(FreeCellNode(
                        counter=self.counter,
                        n=len(self.state),
                        state=pile_helper(
                            pile_num, other_pile_num, self.state),
                        parent=self,
                        path=(self.path + ["%d -> %d" % (pile_num,
                                                         other_pile_num)])))

                # place a lesser block on top of the top block of another pile
                elif pile[-1] <= other_pile[-1] or 0:
                    successors.append(FreeCellNode(
                        counter=self.counter,
                        n=len(self.state),
                        state=pile_helper(
                            pile_num, other_pile_num, self.state),
                        parent=self,
                        path=(self.path + ["%d -> %d" % (pile_num, other_pile_num)])))

        return successors

    def cost(self):
        """ In FreeCell, the cost is the number of moves made. This is g(n) for A*.
        """
        return len(self.path)


if __name__ == "__main__":
    root = FreeCellNode(counter=6, n=3, state=[
        [], [], [5, 4, 3, 2, 1, 6]], path=[])

    def cost_fn(n): return n.cost()

    def dominating_heuristic(node):
        return sum([len(pile) for pile in node.state])

    def simple_heuristic(node): return 1

    print("Running A* using the Dominating Heuristic:")
    print("Node: %s\n Total Nodes Examined: %d" %
          (a_star(root, dominating_heuristic, cost_fn)))

    print("Running A* using the Dominated Heuristic:")
    print("Node: %s\n Total Nodes Examined: %d" %
          (a_star(root, simple_heuristic, cost_fn)))
