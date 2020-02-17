from queue import PriorityQueue
from node import expand_node


def a_star(root, heuristic_fn, cost_fn):
    fringe = PriorityQueue()
    fringe.put((heuristic_fn(root) + cost_fn(root), root))

    nodes_examined = 0
    while not fringe.empty():
        cost, node = fringe.get()
        # print("Cost: %d %s" % (cost, node))
        for successor in node.successors():
            fringe.put((heuristic_fn(successor) +
                        cost_fn(successor), successor))

        nodes_examined += 1
        if node.goal_test():
            # this is a solution.
            return node, nodes_examined

    return None
