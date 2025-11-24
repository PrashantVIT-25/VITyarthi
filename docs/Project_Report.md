# Tideman Voting System: Project Report

## 1. Cover Page

Tideman Voting System

- Cource : Introduction to Problem Solving and Programming
- Cource Code : CSE1021
- Name: Prashant Priydarshi
- Reg. No. : 25BAI11147

## 2. Introduction

In today's elections or situations requiring decision-making, ranked choices determine a fair winner. In such situation, traditional voting systems fail when voters rank the candidates as it leads to inconsistent outcomes. Hence, the tideman voting system was chosen.

## 3. Problem Statement

The core challenge when aggregating ranked votes is designing a method that can consistently compare every candidate pair and resolve circular preferences (like B beats C, C beats A, A beats B) to ultimately select a winner who is undefeated in the final ranking structure, a task traditional majority voting cannot perform accurately.

## 4. Functional Requirements

The system's capabilities are divided into four primary functional modules: Setup,Input Validation, Processing, and Output.

- FR-1: Setup & Initialization: 
The system accepts and initializes the total number of candidates (N) and sets up the global state matrices like preferences, locked, etc.

- FR-2: Data Input & Validation:
The system handles the user's input, validates voter rankings (checks for completeness, uniqueness, and valid names), and converts names into numerical indices.

- FR-3: Preference Processing:
The system aggregates valid rankings into the preference matrix and executes the Tideman steps: generate pairs, sort pairs by margin, and implement cycle-free locking.

- FR-4: Output & Reporting:
The system identifies the source of the final locked graph and displays the name of the Condorcet Winner.

## 5. Non-functional Requirements

- NFR-1 (Maintainability): The codebase adheres to Pythonic standards (PEP 8) and maintains the modular separation of codes (main.py, tideman.py, utils.py) to facilitate future development and auditing.

- NFR-2 (Robustness/Error Handling): The system handles all invalid voter inputs (e.g., duplicate candidate names, non-existent candidates) by terminating and providing a proper "Invalid vote" output.

- NFR-3 (Performance): The algorithmic processing steps (especially the O(N^2) pair operations and recursive checks) executes in near-instantaneous time for typical election sizes (N <= 10).

- NFR-4 (Resource Efficiency): The solution operates purely in-memory, requiring no external libraries or persistent storage, making it lightweight and resource-efficient.

## 6. System Architecture

The project was designed using a Modular CLI Architecture to enforce a clear separation of concerns. This structure was critical for managing the complexity of the core algorithm and keeping the code easily testable. The entire system is built around three distinct functional modules:

- main.py (Controller/I/O Layer): This module handles all communication with the user — taking input and displaying the final winner. Its job is to manage the central flow and acting as the director that sequences the necessary call steps to the other two modules.

- tideman.py (Algorithm/Logic Layer): This file is the project's engine. It holds the core election data and implements every high-level step of the "Tideman algorithm", including the critical "recursive cycle detection" logic.

- utils.py (Helper/Validation Layer): This module isolates simple but necessary tasks, specifically "input validation" and "candidate index lookup" . This keeps the complex logic in tideman.py clean and focused.

The system relies on a central, in-memory Global Election State (the preferences and locked matrices), which is exclusively accessed and modified by the "tideman.py" module.

## 7. Design Diagrams

To document both the static structure and the dynamic behavior of the Tideman system, I created four essential design diagrams. These visuals are critical for auditing the algorithm's control flow and verifying compliance with design principles.

- Workflow Diagram (Process Flow)
This diagram maps the high-level steps of the election process by showing the chronological flow of function calls managed by main.py. It confirms the correct sequencing of the five Tideman steps, illustrating the transition from raw input to the final winner output.

- UML Use Case Diagram
This diagram establishes the scope of the system and the functions it provides to the external world. It defines two key actors—the Administrator and the Voter—and links them to the three primary functionalities of the system: initializing the election, recording preferences, and finding the final winner.

- UML Sequence Diagram
This diagram visualizes the most complex dynamic interaction: the process of recording a single vote. It is crucial because it demonstrates:

    - The flow of control from main.py to utils.py for validation.
    - The use of the Alternative fragment to implement the if/else check on validation success.
    - The subsequent call to tideman.py to update the global state only upon valid input.

As the project is purely an in-memory CLI application and does not utilize any persistent database storage, an Entity-Relationship (ER) Diagram is not applicable.

## 8. Design Decisions & Rationale

I based the design on four key architectural and algorithmic choices to ensure correctness and maintainability.

- Architecture and State
    - Procedural Modularity: I chose Python's procedural structure, splitting the system into three dedicated modules (main, tideman, utils), as this simplifies the model of the sequential Tideman algorithm.

    - Global State Management: The core election data (preferences, locked) is managed via global variables within tideman.py. This ensures the algorithm's sequential steps can efficiently modify a single, central source of truth.

- Algorithmic Implementation
    - Recursive DFS for Cycles: The "creates_cycle" function uses recursion to perform a Depth-First Search. This is the most effective way to trace a path back from the loser to the winner, which is necessary to prevent cycle formation in the locked graph.

    - Testing Focus: The entire strategy centered on unit tests (test1.py) to verify the correct sequencing and the mathematical results of the algorithmic core, guaranteeing the system's output is valid. 

## 9. Implementation Details
The implementation focused on translating the abstract rules of the Tideman algorithm into reliable Python code, with careful attention paid to data structures and the handling of recursion.

- Data Structures and Initial State

The core of the system relies on two dynamic, two-dimensional lists (matrices) initialized based on the total candidate count (N).
    - 'preferences' Matrix: This integer matrix stores vote counts. preferences[i][j] is incremented every time candidate 'i' is ranked above candidate 'j'. This structure is foundational for calculating all pairwise margins.
    - 'locked' Matrix: This boolean matrix represents the final graph of preferences.
    locked[i][j] = True if the edge i -> j was successfully locked without creating a cycle.

- Pair Sorting (sort_pairs)

The 'sort_pairs' function is streamlined using Python's 'sort' method and a 'lambda' key. This allowed me to avoid writing a manual sorting algorithm, focusing instead on defining the critical sorting metric: the margin of victory (votes for W - votes for L). This guarantees that the strongest preferences are checked and locked first, adhering to the Tideman rules.

- Cycle Detection (creates_cycle)

The most delicate part of the implementation is the recursive 'creates_cycle' function. This function performs a Depth-First Search (DFS) starting from the proposed 'loser (L)' to determine if a path already exists that leads back to the 'winner (W)'.
    - Mechanism: The function checks if the current node (L) is the original winner (W); if so, it returns True (cycle detected).
    - Recursion: It recursively follows existing locked edges (locked[current][next_node]) until either the cycle closes or all downstream paths are finished. This precise control flow is essential for a single winner.

- Winner Identification

The 'find_winner' function identifies the winner by iterating through the 'locked' matrix columns. The winner is the candidate index i for which the entire column i is 'False' . This confirms they have no incoming locked edges, meaning no other candidate successfully defeated them in the final preference structure.

## 10. Screenshots / Results

This section provides visual evidence that the Tideman system operates correctly, handles input, and produces the final, verified winner and much more.

- Codebase Structure [Codebase_Structure.png]:
Encapsulates the whole project structure as it is created and labeled.

- End-to-End Execution [main.png]:
This captures a successful run of main.py, showing the input process and the final declared winner.

- Cycle Detection Logic [creates_cycle.png]: 
A visual representation of the core recursive logic for creates_cycle that prevents the graph from looping.

- Validation Error Handling [invalid_vote.png]:
Proof that the system gracefully handles bad data inputs by terminating with a clear error message.

- Unit Test Success [test.png]: 
This screenshot confirms that all 8 unit tests in test1.py successfully passed, guaranteeing the algorithmic stability of the preference calculation, pair sorting, and cycle prevention logic.

- UML Sequence Diagram [Sequence_Diagram.png]:
Verifies the dynamic control flow during vote recording.

- UML Use Case Diagram [Use_Case.png]:
Verifies the system's functional boundaries and external user roles.

- Workflow Diagram [Workflow.png]:
Verifies the high-level sequential flow of the entire Tideman algorithm process.

## 11. Testing Approach

My approach to verifying the system relied heavily on modular unit testing using Python's built-in unittest framework (test1.py). This strategy ensured algorithmic correctness was isolated from input/output concerns.

- Methodology and Coverage
Testing was divided into two main areas:

    - Data Integrity Tests: 
    These focused on the 'utils.py' module, verifying that 'validate_ranks' correctly rejected malformed input (duplicates, incorrect length) and that 'get_candidate_index' provided reliable name-to-index translation.

    - Algorithmic Core Tests:
    These confirmed the mathematical correctness and control flow of the functions in 'tideman.py'.

- Critical Test Cases
The stability of the system hinges on the following three critical test cases:

    - Pair Sorting Verification:
    Tests confirmed that pairs are consistently sorted in descending order based on the margin of victory, which is essential for ensuring the strongest preferences are locked first.
    
    - Winner Identification:
    Tests proved that 'find_winner' correctly identifies the graph's source candidate—the one with no incoming locked edges—across various graph structures.
    
    - Cycle Prevention (The Core Test): The most crucial test case, 'test_lock_pairs_cycle_prevention' , simulates the classic circular dependency (e.g., A -> B, B -> C, C -> A). This test strictly verifies that the recursive Depth-First Search ( 'creates_cycle' ) correctly detects the cycle and forces 'lock_pairs' to skip the final edge, guaranteeing an acyclic graph.


## 12. Challenges Faced

Developing the Tideman system presented two main technical challenges, both related to managing complexity within the Python environment:

- Debugging Recursive Cycle Detection

    - The Challenge:
    The core difficulty lay in debugging the 'creates_cycle' function. Early versions often resulted in either infinite recursion or an incorrect return of 'True' (cycle detected) even when the graph was empty. Identifying the precise flaw in the base case ('winner' == 'loser') and ensuring the recursive call correctly held the target ('winner') constant while updating the current position ('loser') required intensive, step-by-step tracing.

    - The Solution:
    This was solved entirely through focused unit testing. By creating a test case specifically designed to fail on the first, empty pair lock ('test_lock_pairs_cycle_prevention'), I was forced to isolate and correct the parameter passing error in the recursive function call.

- Module Import and Execution Errors

    - The Challenge:
    Due to the modular structure ('src/main.py', 'src/tideman.py'), running the application via the standard command ('python src/main.py') led to the 'ImportError: attempted relative import with no known parent package' .

    - The Solution:
    The issue was resolved by correctly configuring the execution environment. The solution was to always run the file using the module flag ('python -m src.main'), which explicitly tells Python to treat the 'src' directory as the top-level package, successfully resolving all internal relative imports.

## 13. Learnings & Key Takeaways

Completing the Tideman project provided a comprehensive experience in translating complex socio-political theory into functional, verifiable code. The key takeaways from this implementation include:

- Algorithmic Mastery
    - Graph Theory in Practice:
    I gained practical expertise in applying Depth-First Search (DFS) to a non-standard problem—specifically, using recursion to check for cycles in a preference graph. This demonstrated the power of recursion to solve complex pathfinding challenges.

    - Understanding Condorcet Methods:
    The project enforced a strong understanding of why the Tideman method is superior to simple majority voting, specifically how it prioritizes the Condorcet Winner by resolving the inconsistencies of circular preferences.

- Software Engineering Skills
    - Modular Design: I reinforced the importance of the separation of concerns by strictly isolating Input/Output ('main.py'), Validation ('utils.py'), and Core Logic ('tideman.py'). This guarantees high code maintainability and clarity.

    - Defensive Testing: The necessity of thorough unit testing became clear, particularly for fragile recursive algorithms. Writing tests for edge cases, like the cycle-prevention logic, proved essential for ensuring the system's output is mathematically sound and reliable.

    - Execution Environment Control: I mastered the nuances of managing Python execution environments and module imports, resolving complex issues like the 'ImportError' by correctly running the project using the module flag ('python -m').

## 14. Future Enhancements

- Future Enhancements:
    While the core algorithmic goal has been achieved, several enhancements could significantly expand the project's utility and complexity, addressing features omitted in the initial scope.

    - Interface and Usability:

        - GUI Development: The current Command-Line Interface (CLI) is functional but limited. The project could be transitioned to a simple Graphical User Interface (GUI), providing a more user-friendly way to input candidate lists and visualize the final results.

        - Real-Time Visualization: Integrate a front-end component to dynamically visualize the locked graph as pairs are confirmed. This would show the preference flow and the point at which a cycle is detected, offering valuable insight for educational purposes.

    - Algorithmic Refinement

        - Tie Handling Implementation: The current specification assumes no ties in head-to-head counts. A future enhancement would be to implement a formal tie-breaking mechanism (e.g., breaking the tie based on the smallest number of voters who prefer the tied pair, or a random selection) to ensure consistency even when margins are equal.

        - Ranking Abstraction: Modify the input system to handle incomplete or partial rankings (e.g., a voter ranking only their top three candidates), requiring changes to how the preferences matrix is updated.

    - Data Management

        - Persistent Storage: Transition from the current in-memory Global Election State to a persistent storage solution (like a local SQLite database). This would allow elections to be paused, resumed, and audited across different sessions, fulfilling a major enterprise requirement. This would also necessitate the design and inclusion of an Entity-Relationship (ER) Diagram in future documentation.

## 15. References

The following sources were instrumental in defining the Tideman method's rules and establishing the correct implementation structure for cycle detection:

- Tideman, T. N. (1987). 
Independence of Clones as a Criterion for Voting Rules. Social Choice and Welfare, 4(3), pp. 185-206. (Source for the formal definition of the Ranked Pairs/Tideman method.)

- Wikipedia,(2025) Ranked pairs. 
Retrieved from [https://en.wikipedia.org/wiki/Ranked_pairs]. (Used for general algorithmic overview and terminology.)

- CS50x (Harward). (Used for implementation structure and the standard model for global state management and recursive cycle checking in Python/C).

- Tool/Library Citation: Python Software Foundation (2025), unittest module. (Used for defining the testing approach and methodology.)