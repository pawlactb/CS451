from node import Node, create_finite_tree
from random import shuffle
from copy import deepcopy
from queue import Queue, LifoQueue


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
            back_word = self.words_added[i+1]

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


def BFS(root):
    node_num = 0
    fringe = Queue()

    # put the root on the fringe
    fringe.put(root)

    # in BFS, we treat the fringe as a FIFO queue
    while not fringe.empty():
        node = fringe.get()
        node_num += 1
        print("Examining Node #%d: %s" % (node_num, node))
        for child in node.children:
            fringe.put(child)
        if node.goal_check():
            return node


def DFS(root):
    node_num = 0
    fringe = LifoQueue()

    # put the root on the fringe
    fringe.put(root)

    # in DFS, we treat the fringe as a LIFO queue
    while not fringe.empty():
        node = fringe.get()
        node_num += 1
        print("Examining Node #%d: %s" % (node_num, node))
        for child in node.children:
            fringe.put(child)
        if node.goal_check():
            return node


def main():
    word_set = ["apple", "egress", "state", "exit", "transformer"]
    shuffle(word_set)
    root_node = geography_node(word_set, [], name="root")

    print(root_node.goal_test())

    create_finite_tree(root_node)

    print(BFS(root_node))

    print(DFS(root_node))


if __name__ == "__main__":
    main()
