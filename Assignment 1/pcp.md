# PCP Problem Solution

## Tyler Pawlaczyk

### Student #0527039 pawlactb@clarkson.edu

- See other files in archive for source code. node.py and search.py contains files for both problems, pcp.py contains source specific to the post-correspondance problem.

## Definitions

- State
  - state in the geography problem is represented as two strings - the top row and the bottom row.
- Initial State
  - The initial state has a set of dominoes, and a domino with a non-empty top and bottom. Any state is a valid initial state.
- Goal Test
  - The goal test compares the top to the bottom, and succeeds if they are equal.
- Successor Function
  - the successor function will return a list of nodes such that the state of each node has the parent's top and bottom row, with one of the dominoes appended for each successor node.
