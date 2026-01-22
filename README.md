# Sudoku Solver with CSP Techniques

## 🧩 Project Overview

This repository contains a Python implementation of a Sudoku solver using Constraint Satisfaction Problem (CSP) techniques. The solver employs backtracking search enhanced with the Minimum Remaining Values (MRV) heuristic and forward checking for efficient puzzle solving.

## 🎯 Features

- **Backtracking Algorithm**: Core search algorithm for solving Sudoku puzzles
- **MRV Heuristic**: Selects cells with the smallest domain first to reduce branching factor
- **Forward Checking**: Maintains arc consistency by pruning domains during search
- **Constraint Validation**: Complete row, column, and subgrid constraint checking
- **Error Detection**: Identifies unsolvable and invalid puzzles
- **Performance**: Solves most puzzles in under 1.2 seconds

## 📊 Algorithm Comparison

| Characteristic | Brute-Force | Our Backtracking Implementation |
|----------------|-------------|----------------------------------|
| **Efficiency** | Extremely inefficient (up to 9⁸¹ combinations) | Highly efficient with CSP enhancements |
| **Implementation** | Simple random assignment | Sophisticated with MRV and forward checking |
| **Hardware Requirements** | Very taxing (stores all attempts) | Minimal memory usage |
| **Improvability** | Hardware-dependent only | Can be enhanced with additional CSP techniques |
| **Typical Solve Time** | Impractical for real use | < 1.2 seconds for most puzzles |

## 🏗️ Architecture

### Formal CSP Definition

**Variables**: 81 cells `C_ij` where `i, j ∈ {1,2,...,9}` (row, column indices)

**Domains**: 
- Empty cells: `D_ij ∈ {1,2,...,9}`
- Pre-filled cells: `D_ij = {value}`

**Constraints**:
1. **Row Constraint**: All values in a row must be unique
2. **Column Constraint**: All values in a column must be unique  
3. **Subgrid Constraint**: All values in a 3×3 subgrid must be unique

### Implemented Techniques

#### 1. **Constraint Checking Functions**
- Validates row, column, and subgrid uniqueness
- Used during forward checking and solution verification

#### 2. **Domain Management**
- Tracks possible values for each empty cell
- Dynamically updates domains during search

#### 3. **MRV (Minimum Remaining Values) Heuristic**
- Selects the cell with the fewest legal values first
- Reduces branching factor and search space

#### 4. **Forward Checking**
- After assignment, removes value from domains of constrained cells
- Detects dead ends early to avoid futile search paths

#### 5. **Backtracking Search**
- Recursive depth-first search with intelligent variable/value ordering
- Backtracks when constraint violation detected

## 📁 File Structure

```
sudoku_solver/
├── sudoku_solver.py      # Main solver implementation
├── utils.py              # Utility functions
├── test_puzzles.py       # Test suite with various difficulty levels
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## 🚀 Usage

### Basic Usage
```python
from sudoku_solver import solve_sudoku

# Define puzzle as 9x9 grid (0 represents empty cell)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solution, time_taken = solve_sudoku(puzzle)
print(f"Solved in {time_taken:.3f} seconds")
print_sudoku(solution)
```

### Command Line Interface
```bash
python sudoku_solver.py --puzzle easy   # Solve easy puzzle
python sudoku_solver.py --puzzle hard   # Solve hard puzzle
python sudoku_solver.py --file puzzle.txt  # Solve from file
```

## 📊 Performance

### Test Results
- **Easy Puzzles**: < 0.1 seconds
- **Medium Puzzles**: 0.1-0.5 seconds  
- **Hard Puzzles**: 0.5-1.2 seconds
- **Expert Puzzles**: Up to 1.2 seconds

### Edge Cases Handled
1. **Unsolvable Puzzles**: Returns appropriate error message
2. **Invalid Puzzles**: Detects constraint violations in initial state
3. **Already Solved Puzzles**: Returns immediately with verification
4. **Multiple Solutions**: Finds one valid solution (standard Sudoku assumption)

## 🔍 Why Not Other Algorithms?

### A* Search
- **Not suitable** for Sudoku as it's a constraint satisfaction problem, not pathfinding
- No clear way to define cost and heuristic functions
- Would be less efficient than CSP techniques

### Machine Learning
- Requires large dataset of solved puzzles
- Computationally expensive for training
- Complex implementation compared to backtracking
- Less interpretable than algorithmic approach

### Brute Force
- Theoretically tries 9⁸¹ combinations (≈ 2×10⁷⁷)
- Completely impractical for real-world use
- No intelligent pruning or constraint propagation

## 🛠️ Implementation Details

### Key Functions

```python
def solve_sudoku(board):
    """Main solving function with backtracking, MRV, and forward checking"""
    
def get_mrv_cell(board, domains):
    """Selects cell with minimum remaining values using MRV heuristic"""
    
def forward_check(board, cell, value, domains):
    """Propagates constraints and updates domains after assignment"""
    
def is_valid(board, row, col, num):
    """Checks if number placement violates constraints"""
    
def get_subgrid(board, row, col):
    """Extracts 3x3 subgrid for constraint checking"""
```

### Data Structures
- **Board**: 9×9 list of integers (0 for empty)
- **Domains**: Dictionary mapping cells to sets of possible values
- **MRV Queue**: Priority queue for cell selection

## 🧪 Testing

The solver includes comprehensive testing:
```python
# Run test suite
python test_puzzles.py

# Test categories:
# - Easy puzzles (basic backtracking sufficient)
# - Medium puzzles (MRV provides benefit)
# - Hard puzzles (forward checking essential)
# - Expert puzzles (tests all optimizations)
# - Invalid/Unsolvable puzzles (error handling)
```

## 📈 Optimization Opportunities

Potential enhancements (not implemented):
1. **Arc Consistency (AC-3)**: Further domain reduction
2. **Least Constraining Value (LCV)**: Better value ordering
3. **Constraint Propagation**: More sophisticated inference
4. **Parallel Processing**: Multi-threaded search for hardest puzzles

## 📚 References

1. Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Chapter 6: Constraint Satisfaction Problems.
2. Sudoku solving algorithms and CSP techniques
3. Backtracking search optimizations for constraint satisfaction

## 👥 Authors

**Rayyan Ali Ahmed**
**Basil Rehan Siddiqui**
