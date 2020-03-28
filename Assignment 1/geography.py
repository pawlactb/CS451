from node import Node
from random import shuffle
from copy import deepcopy
from queue import Queue, LifoQueue
from search import BFS, DFS


class geography_node(Node):
    def __init__(self, words_left, words_added, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.words_left = words_left
        self.words_added = words_added

    def __str__(self):
        return "Geography Node\n" + ("parent: %s\n" % (self.parent.name if self.parent else "root")) + ("words_left: %s, words_added: %s\n" %
                                                                                                        (self.words_left, self.words_added))

    def goal_test(self):
        if not len(self.words_left) == 0:
            return False

        for i in range(0, len(self.words_added) - 1):
            front_word = self.words_added[i]
            back_word = self.words_added[i + 1]

            if not front_word[-1] == back_word[0]:
                return False
        return True

    def successors(self):
        next = []
        for word in self.words_left:
            w_a = deepcopy(self.words_added) + [word]
            w_l = deepcopy(self.words_left)
            w_l.remove(word)
            next.append(geography_node(
                words_left=w_l,
                words_added=w_a,
                parent=self))
        return next


def main():
    test_case_1 = ["CDE", "CFG", "EHE", "EIJ", "GHK", "GLC"]
    test_case_2 = ["CDE", "CFG", "EHI", "GJC", "GKG"]

    root_node_1 = geography_node(test_case_1, words_added=["ABC"], name="root")

    print("BFS of Test Case 1:")
    print("Result of BFS on Test Case 1: %s, nodes visited: %d\n" %
          (BFS(root_node_1, node_count_max=128)))
    print("DFS of Test Case 1:")
    print("Result of DFS on Test Case 1: %s, nodes visited: %d\n" %
          (DFS(root_node_1, node_count_max=128)))

    root_node_2 = geography_node(test_case_2, words_added=["ABC"], name="root")

    print("BFS of Test Case 2:")
    print("Result of BFS on Test Case 2: %s, nodes visited: %d\n" %
          (BFS(root_node_2, node_count_max=128)))
    print("DFS of Test Case 2:")
    print("Result of DFS on Test Case 2: %s, nodes visited: %d\n" %
          (DFS(root_node_2, node_count_max=128)))


if __name__ == "__main__":
    main()
