# CS Data Structures & Algorithms (From Scratch)

This repository contains my from-scratch implementations of core Computer Science data structures and algorithms.  
The goal is to demonstrate strong fundamentals in data organization, algorithmic efficiency, and problem-solving.

## Repository Structure
- `data_structures/` — Arrays, Linked List, Stack, Queue, BST, Graph
- `algorithms/` — Searching, Sorting, BFS/DFS traversal
- `tests/` — Basic test scripts to validate correctness

## Implemented Data Structures
- Arrays
- Linked Lists
- Stack (LIFO)
- Queue (FIFO)
- Binary Search Tree (insert/search/traversal)
- Graph (Adjacency List)

## Implemented Algorithms
- Searching: Linear Search, Binary Search
- Sorting: Bubble Sort, Merge Sort, Quick Sort
- Graph Traversal: BFS, DFS

## Complexity Overview (Big-O)
| Topic | Operation | Time Complexity |
|------|-----------|-----------------|
| Array | Access | O(1) |
| Linked List | Search | O(n) |
| Stack | Push/Pop | O(1) |
| Queue | Enqueue/Dequeue | O(1)\* |
| BST | Insert/Search (avg) | O(log n) |
| BST | Insert/Search (worst) | O(n) |
| Linear Search | Search | O(n) |
| Binary Search | Search (sorted) | O(log n) |
| Bubble Sort | Sort | O(n²) |
| Merge Sort | Sort | O(n log n) |
| Quick Sort | Sort (avg) | O(n log n) |

\*Note: Queue can be optimized further using `collections.deque` for efficient front removals.

## How to Run
This project uses Python 3.

### Run the algorithm tests
From the repository root, run:
```bash
python3 tests/test_algorithms.py
