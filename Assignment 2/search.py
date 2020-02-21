from queue import PriorityQueue
from node import expand_node


def a_star(root, heuristic_fn, cost_fn):
    fringe = PriorityQueue()
    fringe.put((cost_fn(root) + heuristic_fn(root), root))
    visited = []
    nodes_examined = 0
    while not fringe.empty():
        cost, node = fringe.get()

        nodes_examined += 1

        if node.goal_test():
            # this is a solution.
            return node, nodes_examined

        for successor in node.successors():
            # print("added successor!")
            if node in visited:
                continue
            else:
                visited.append(node)
                fringe.put(
                    (cost_fn(successor) + heuristic_fn(successor), successor))

    return None, nodes_examined
