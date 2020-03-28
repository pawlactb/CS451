from search import BFS, DFS
from queue import Queue, LifoQueue
from copy import deepcopy
from random import shuffle
from node import Node


class pcp_node(Node):
    def __init__(self, dominoes, top=None, bottom=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dominoes = deepcopy(dominoes)
        self.top = str(top)
        self.bottom = str(bottom)

    def __str__(self):
        return ("top: %s, bottom: %s" % (self.top, self.bottom))

    def goal_test(self):
        return self.top == self.bottom

    def successors(self):
        next = []
        for top, bottom in self.dominoes:
            next.append(pcp_node(
                self.dominoes,
                top=(self.top + top),
                bottom=(self.bottom + bottom),
                parent=self,
                path=self.path + [(top, bottom)]))
        return next


def traverse(root):
    print(root)
    for node in root.children:
        traverse(node)


def main():

    test_case_1 = [("MOM", "M"), ("O", "OMOMO")]
    root_node_1 = pcp_node(test_case_1, top="MOM", bottom="M", name="root")

    print("BFS of Test Case 1:")
    print("Result of BFS on Test Case 1: %s, nodes visited: %d\n" %
          (BFS(root_node_1, node_count_max=128)))
    print("DFS of Test Case 1:")
    print("Result of DFS on Test Case 1: %s, nodes visited: %d\n" %
          (DFS(root_node_1, node_count_max=128)))

    test_case_2 = [("AA", "A")]
    root_node_2 = pcp_node(test_case_2, top="AA", bottom="A", name="root")

    print("BFS of Test Case 2:")
    print("Result of BFS on Test Case 2: %s, nodes visited: %d\n" %
          (BFS(root_node_2, node_count_max=128)))
    print("DFS of Test Case 2:")
    print("Result of DFS on Test Case 2: %s, nodes visited: %d\n" %
          (DFS(root_node_2, node_count_max=128)))


if __name__ == "__main__":
    main()
