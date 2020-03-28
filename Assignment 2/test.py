from freecell import FreeCellNode
from search import a_star


def cost_fn(n): return n.cost()


def dominating_heuristic(node):
    cost = 0
    for pile in node.state:
        if len(pile) <= 1:
            cost += len(pile)
        else:
            cost += len(pile) - 1 + len(pile)
    return cost


def dominated_heuristic(node):
    return sum([len(pile) for pile in node.state])


if __name__ == "__main__":
    # test case structure: ([piles], n, counter)
    test_cases = [([[], [], [4, 5, 1, 2, 6, 7, 10, 9, 3, 8]], 3, 10)]

    test_case = 0

    for state, n, counter in test_cases:
        test_case += 1
        print("\nTest Case: %d" % (test_case))

        root = FreeCellNode(counter=counter, n=n,
                            state=state, path=[], root=True)
        # print(root)

        print("Running A* using the Dominating Heuristic:")
        try:
            print("Node: %s\n Total Nodes Examined: %d" %
                  (a_star(root, dominating_heuristic, cost_fn)))
        except TypeError:
            print("No Solution Found.")
            continue
