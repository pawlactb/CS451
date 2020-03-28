from queue import PriorityQueue, Queue, LifoQueue

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


def BFS(root, node_count_max=None):
    node_num = 0
    fringe = Queue()

    # put the root on the fringe
    fringe.put(root)

    # in BFS, we treat the fringe as a FIFO queue
    while not fringe.empty() and node_num < node_count_max:
        node = fringe.get()
        node_num += 1
        print("Examining Node #%d: %s" % (node_num, node))
        for child in node.successors():
            node.register_child(child)
            fringe.put(child)
        if node.goal_test():
            return node, node_num
    return None, node_num


def DFS(root, node_count_max=None):
    node_num = 0
    fringe = LifoQueue()

    # put the root on the fringe
    fringe.put(root)

    # in DFS, we treat the fringe as a LIFO queue
    while not fringe.empty() and node_num < node_count_max:
        node = fringe.get()
        node_num += 1
        print("Examining Node #%d: %s" % (node_num, node))
        for child in node.children:
            fringe.put(child)
        if node.goal_test():
            return node, node_num
    return None, node_num
