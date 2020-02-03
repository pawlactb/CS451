class Node(object):
    def __init__(self, name=None, parent=None, action_generated=None, total_path_cost=0):
        self.parent = parent
        self.fringe = []
        self.action_generated = action_generated
        self.total_path_cost = 0
        self.name = name
        self.children = []

    def register_child(self, child):
        self.children.append(child)

    def is_valid(self):
        pass

    def is_complete(self):
        pass

    def goal_test(self):
        pass

    def successors(self):
        pass


def create_finite_tree(root):
    successors = root.successors()
    for node in successors:
        node.parent.register_child(node)
        create_finite_tree(node)


def expand_node(node):
    successors = node.successors()
    for s in successors:
        s.parent.register_child(s)
