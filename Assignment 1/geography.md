# Geography Problem Solution

## Tyler Pawlaczyk

### Student #0527039 pawlactb@clarkson.edu

- See other files in archive for source code. node.py contains files for both problems, geography.py contains source specific to the geography problem.

## Definitions

- State
  - state in the geography problem is represented as two lists - a list of words to be added, and a list of words already added.
- Initial State
  - The initial state has a populated list of words to be added, and no words added.
- Goal Test
  - The goal test examines the list of added words and ensures that the last letter of each word is the same as the first of the next. The goal test will fail if the words to be added list is not empty.
- Successor Function
  - the successor function will return a list of states such that the current list of words added, each with one (different) word added from the words to be added list.
