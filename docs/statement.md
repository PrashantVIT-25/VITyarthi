# Problem Statement

## 1. Introduction
In today's elections or situations requiring decision-making, ranked choices determine a fair winner. In such situation, traditional voting systems fail when voters rank the candidates as it leads to inconsistent outcomes.

## 2. The Problem
When voters rank the candidates (C > B > A etc.), we need a method to:
- Compare every pair of candidates,
- Determine the preferred in each pair,
- Avoid cycles in rankings (B beats C, C beats A, A beats B),
- Select a winner who is not defeated by any other candidate in the final graph.

A traditional majority vote system cannot do this accurately.

## 3. Tideman Method
The Tideman (Ranked Pairs) algorithm solves this problem by:
- Recording the preferences of each voter,
- Creating different "winner-loser" pairs,
- Locking the pairs such they don't form cycles,
- Declaring the candidate without any edges pointing to them as the final winner.

## 4. Why This Project?
This method has many real-world application in different systems:
- Ranked-choise elections,
- Student council selections,
- Committee decisions,
- Multi-criteria decisions,

It demonstrates thinking algorithmically.

## 5.Project Goal
To design and implement the Tideman voting system using Python language with top-down approach:
- Defining the problem
- Requirement analysis
- Algorithm design
- Implementation
- Testing and Debugging

The final system must accept ranked votes as the input and produce a signal a clear and fair winner.
