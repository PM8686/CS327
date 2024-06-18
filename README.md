# CPSC 327 (FA23): Object-Oriented Programming

**Course Description:** Object-oriented programming (OOP) focuses on designing and writing efficient, reliable, modular, and reusable code using core concepts and features such as classes, inheritance, composition, encapsulation, polymorphism, and exceptions. The course also covers the use of object-oriented design patterns like iterator, decorator, strategy, adapter, and observer. The primary language for the course is Python, with comparisons to other languages such as C++.

---

## Homework 1 - Classes and Relationships
**Objective:** Implement a simple Bank application with a command line interface (CLI) to get up to speed with Python and OOP.

**Key Features:**
- **CLI:** Developed a command line interface in `cli.py` that implements the read-eval-print loop (REPL).
- **Classes:** Implemented multiple classes including `Bank`, `Account`, `CheckingAccount`, `SavingsAccount`, and `Transaction`.
- **Relationships:** Established relationships between classes to manage different types of bank accounts and their transactions.
- **UML:** Described the design with UML diagrams.
- **Persistence:** Implemented file operations and object serialization using pickle.

---

## Homework 2 - Exceptions and Logging
**Objective:** Enhance the Bank application by handling edge cases using exceptions and adding logging functionality.

**Key Features:**
- **Exceptions:** Utilized exceptions to handle various edge cases such as invalid transactions, overdrawing accounts, and improper date formats.
- **Custom Exceptions:** Introduced custom exceptions like `OverdrawError` and `TransactionSequenceError`.
- **Logging:** Configured a logger to record debug messages and handled unexpected errors with user-friendly messages and detailed logs.

---

## Homework 3 - GUIs and ORMs
**Objective:** Extend the Bank application to use a database and create a graphical user interface (GUI).

**Key Features:**
- **SQLite & SQLAlchemy:** Integrated SQLite for persistent storage and SQLAlchemy as an ORM to manage database interactions.
- **ORM Models:** Converted classes into ORM models, defined table structures, and managed relationships using SQLAlchemy.
- **GUI with tkinter:** Developed a GUI using tkinter, allowing users to interact with the bank application through a graphical interface.
- **Exception Handling:** Adapted exception handling for the GUI context, displaying errors in popups.

---

## Homework 4 - Unit Testing
**Objective:** Write unit tests for an Enigma machine simulator to ensure code reliability and measure coverage.

**Key Features:**
- **Test Cases:** Developed a comprehensive test suite covering all methods in `machine.py` and `components.py`.
- **Coverage:** Achieved 100% branch coverage using the coverage tool.
- **Bug Detection:** Wrote tests to effectively catch intentional bugs introduced during grading.

---

## Homework 5 - Iterator/Decorator in C++
**Objective:** Practice C++ and implement the Iterator and Decorator design patterns with SmartPointers.

**Key Features:**
- **SmartPointers:** Implemented SmartPointers to manage memory through reference counting.
- **Memory Management:** Fixed a provided LinkedList implementation to use SmartPointers and avoid memory leaks.
- **Garbage Collection:** Demonstrated a simple garbage collection mechanism and identified limitations with cyclic references.

---

## Homework 6 - Design Patterns
**Objective:** Design and implement a Santorini game using design patterns and build AI players.

**Key Features:**
- **Game Implementation:** Designed the class structure for a Santorini game, enabling two human players to play via CLI.
- **Game Logic:** Implemented game rules, move validation, and end conditions.
- **AI Players:** Created two types of AI players (Random and Heuristic) to play the game. The Heuristic player uses a weighted scoring system to evaluate moves.
