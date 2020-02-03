from node import Node, expand_node
from random import shuffle
from copy import deepcopy
from queue import Queue, LifoQueue


class pcp_node(Node):
    def __init__(self, dominoes, top=None, bottom=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dominoes = dominoes
        self.top = top
        self.bottom = bottom

    def __str__(self):
        return "PCP Node\n" + ("parent: %s\n" % (self.parent.name if self.parent else "root")) + ("top: %s, bottom: %s\n" %
                                                                                                  (self.top, self.bottom))

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
                action_generated=(top, bottom)))
        return next


def traverse(root):
    print(root)
    for node in root.children:
        traverse(node)


def BFS(root):
    node_num = 0
    fringe = Queue()

    # expand root
    expand_node(root)

    # put the root on the fringe
    fringe.put(root)

    # in BFS, we treat the fringe as a FIFO queue
    while not fringe.empty() and node_num < 40:
        node = fringe.get()
        node_num += 1
        expand_node(node)
        print("Examining Node #%d: %s" % (node_num, node))
        for child in node.children:
            fringe.put(child)
        if node.goal_test():
            return node


def DFS(root):
    node_num = 0
    fringe = LifoQueue()

    # expand root
    expand_node(root)

    # put the root on the fringe
    fringe.put(root)

    # in DFS, we treat the fringe as a LIFO queue
    while not fringe.empty() and node_num < 40:
        node = fringe.get()
        node_num += 1
        expand_node(node)
        print("Examining Node #%d: %s" % (node_num, node))
        for child in node.children:
            fringe.put(child)
        if node.goal_test():
            return node


def main():

    dominoes = [("0101", "01"), ("1", "01101")]
    root_node = pcp_node(dominoes, top="0101", bottom="01", name="root")

    print(root_node.goal_test())

    print(BFS(root_node))

    # print(DFS(root_node))


if __name__ == "__main__":
    main()