# CS451/CS551/EE565 Homework 1 - due Sunday February 2, 2020

You need to solve the following two problems in a programming language of your choice:

1. Geography Problem
2. PCP Problem

For each problem, you need to define:

1. State
2. Initial State
3. Goal Test
4. Successor Function

----

For each of the problems you must write a BFS algorithm and a DFS algorithm that uses the problem definition and tries to solve the problem.  Recall that completeness issues, time complexity and space complexity may prevent your program from solving the problem.

For each problem, you must turn in the following:

1. Your code
2. An English description of state, initial state, goal test and successor function
3. Program output of the solutions to the test problems that I will give you later
4. Output from your program indicating what order the nodes are visited for my test cases

Note that for the fourth part you must print out the states as they are visited.

----

Here is a description of each of the problems:

## Geography Problem

You have a set of words.  A list of words in legal if the last letter of each word is the same as the first letter of the following word. The problem is to find a legal list of words using all the words exactly once.  Assume that initially the first word is there, and you just need to complete it.

## PCP Problem

You have a set of dominoes.  Each one contains a string on the top and a string on the bottom. The problem is to find a sequence of dominoes such that the concatenation of the strings on the top gives the same string as the concatenation of all the strings on the bottom.  Dominoes may be used as many times as you want.  Assume that the first word is there.

## Test Cases

### Geography

1. ABC, CDE, CFG, EHE, EIJ, GHK, GLC.  Initial word is ABC
2. ABC, CDE, CFG, EHI, GJC, GKG.  Initial word is ABC

### PCP

1. (MOM,M) (O,OMOMO).  Initial domino is (MOM,M)
2. (AA,A).  Initial domino is (AA, A)
