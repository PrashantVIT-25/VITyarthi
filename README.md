# Tideman Voting System (Python)

## Overview
The project implements a Ranked Pair (Tideman) Voting method using Python.
The goal is to determine a fair election winner from ranked voter preferences without cycles.

## Current Status
Documentation complete.
Core algorithm and modules complete.
Test algorithm complete.

## Project Structure
project/
  ├── src/
  |    ├── __init__.py
  |    ├── main.py
  |    ├── tideman.py
  |    ├── utils.py
  ├── docs/
  |    ├── Problem_Statement.md
  |    ├── Project_Report.md
  ├── screenshots/
  |    ├── Codebase Structure.png
  |    ├── creates_cycle.png
  |    ├── invalid_vote.png
  |    ├── main.png
  |    ├── Sequence Diagram.png
  |    ├── test.png
  |    ├── Use Case.png
  |    ├── Workflow.png
  ├── tests/
  |    ├── test1.py
  ├── README.md

## Features

- Input Handling: Accepts candidate and the voter's preferences
- Data Handling: Robustly checks for invalid votes.
- Core Logic: Implements all five steps of the Tideman algorithm: preference recording, pair creation, margin sorting, cycle-free locking, and winner determination.
- Cycle Prevention: Uses recursive Depth-First Search (DFS) to ensure the final locked graph is acyclic.
- Condorcet Winner Guarantee: Guarantees that the Condorcet winner is found, if one exists. 

## Technologies/Tools Used
List the software required to run and test the project.

- Language: Python 3.x
- Testing: unittest (Standard Python Library)
- Dependencies: None (Pure Python implementation)
- Environment: Virtual Environment (venv)

## Steps to Install & Run the Project

- Clone the repository
  '''bash
  git clone [URL_of_Repo]
  cd project
  '''

- Create and activate a virtual environment:
  '''bash
  python3 -m venv venv

  source venv/bin/activate # macOS/Linux

  OR   

  .\venv\Scripts\activate # Windows

- Run the Application:
  '''bash
  python3 -m src.main
  '''

## Running Unit Tests

To verify the core logic of the Tideman Algo(pair sorting, cycle detection, winner finding) , run the included test suite:

- Ensure your virtual environment is active.
- Execute the tests:
  '''bash
  python3 -m unittest tests.test1
  '''

  A successful run will confirm that all 8 test cases, including the cycle-prevention logic, have passed.